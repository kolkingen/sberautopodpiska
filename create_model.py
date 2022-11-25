"""
Скрипт для создания модели. 
"""


from typing import Tuple, Dict, Union
from pathlib import Path
from datetime import datetime
from os import PathLike

import pandas as pd
import dill
from lightgbm import LGBMClassifier
# для подготовкии и оценки модели
from sklearn.metrics import (
    roc_auc_score, accuracy_score, precision_score, recall_score, f1_score)
from sklearn.model_selection import train_test_split
from sklearn.base import BaseEstimator
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler
from feature_engine.selection import (
    DropFeatures, DropDuplicateFeatures, 
    DropCorrelatedFeatures, DropConstantFeatures)
from feature_engine.encoding import RareLabelEncoder, OneHotEncoder
from feature_engine.wrappers import SklearnTransformerWrapper
from feature_engine.outliers import Winsorizer
from feature_engine.transformation import YeoJohnsonTransformer

import additional_data as add


# Информация о модели
RANDOM_SEED = 0
VERSION = 1.0
AUTHOR = 'Nikolai Borziak'
NAME = 'SberAutopodpiska: target event prediction'
DESCRIPTION = '''
    Модель по предсказанию совершения пользователем одного из 
    целевых действий "Заказать звонок" или "Оставить заявку"
    на сайте сервиса СберАвтоподписка.''' 

# Укажем путь к данным и к папке с моделями
DATA_FOLDER = Path('data')
SESSIONS_FILENAME = 'ga_sessions.csv'
HITS_FILENAME = 'ga_hits.csv'
MODELS_FOLDER = Path('models')

# Тип для метаданных
_metadata_type = Dict[str, Union[str, float, Dict[str, float]]]


def create_model(
    data_folder: Union[PathLike, None] = None, 
    models_folder: Union[PathLike, None] = None
) -> None:
    """Создаёт, обучает и сохраняет модель."""

    # Получение данных и создание модели 
    X, y = _load_data(data_folder or DATA_FOLDER)
    model = _get_model()

    # Метаданные и метрики модели
    metadata = _get_metadata(model, X, y)

    # Обучение модели на всех данных
    model.fit(X, y)

    # Сохранение модели с метаданными
    _save_model(model, metadata, models_folder or MODELS_FOLDER)


def _load_data(folder: PathLike) -> Tuple[pd.DataFrame, pd.Series]:
    """Загружает данные из файлов с сессиями и событиями."""
    
    sessions_file = Path(folder) / SESSIONS_FILENAME
    hits_file = Path(folder) / HITS_FILENAME

    # Загрузка файлов (если существуют)
    for file in (sessions_file, hits_file):
        if not file.exists():
            raise FileNotFoundError(f'Не найден файл {file}')
    sessions = pd.read_csv(sessions_file)
    hits = pd.read_csv(hits_file, usecols=['session_id', 'event_action'])

    # Получение целевой переменной
    hits['target'] = hits['event_action'].isin(add.target_events)
    is_target_event = hits.groupby('session_id')['target'].any().astype(float)
    target = pd.Series(is_target_event, index=sessions['session_id'])

    return sessions, target.fillna(0.0)


def _get_model() -> BaseEstimator:
    """Возвращает модель с гиперпараметрами, найденными в ноутбуке 
    с исследованием модели `notebooks/model_research.ipynb`.
    """

    return Pipeline(steps=[
        # Создание дополнительных признаков и
        # Приведение датафрейма к удобному виду 
        ('indexer', FunctionTransformer(_set_index)), 
        ('imputer', FunctionTransformer(_fill_missings)), 
        ('engineer', FunctionTransformer(_create_features)), 
        ('dropper', DropFeatures(['client_id', 'visit_date', 'visit_time', 
                                  'device_screen_resolution'])), 
        # Преобразования численных переменных
        ('normalization', YeoJohnsonTransformer()), 
        ('outlier_remover', Winsorizer()), 
        ('scaler', SklearnTransformerWrapper(StandardScaler())), 
        # Преобразования категориальных признаков
        ('rare_encoder', RareLabelEncoder(tol=0.05, replace_with='rare')),
        ('onehot_encoder', OneHotEncoder(drop_last_binary=True)), 
        ('bool_converter', FunctionTransformer(_converse_types)), 
        # Удаление дубликатов и коррелируемых признаков
        ('constant_dropper', DropConstantFeatures(tol=0.99)), 
        ('duplicated_dropper', DropDuplicateFeatures()), 
        ('correlated_dropper', DropCorrelatedFeatures(threshold=0.95)), 
        # Лучшая модель с оптимизированными гиперпараметрами
        ('model', LGBMClassifier(
            n_estimators=800, learning_rate=0.07, reg_lambda=10, reg_alpha=10, 
            num_leaves=26, boosting_type='goss', random_state=RANDOM_SEED))])


def _set_index(data: pd.DataFrame, column: str = 'session_id') -> pd.DataFrame:
    """Устанавливает в качестве индекса датафрейма колонку `column`."""
    
    data = data.copy()

    if column in data.columns:
        data = data.set_index(column)
    
    return data


def _fill_missings(data: pd.DataFrame) -> pd.DataFrame:
    """Заполняет пропущенные значения:
    * самым частым значением для `device_screen_resolution`;
    * значением '(nan)' во всех остальных случаях.
    """

    data = data.copy()

    if 'device_screen_resolution' in data.columns:
        # '414x896' - мода 'device_screen_resolution' согласно анализу
        data['device_screen_resolution']\
            .replace(add.missing_values, '414x896', inplace=True)
    
    return data.fillna('(nan)')


def _create_features(data: pd.DataFrame) -> pd.DataFrame:
    """Создаёт новые признаки из существующих."""

    data = data.copy()
    
    # visit_date признаки 
    if 'visit_date' in data.columns:
        data['visit_date'] = data['visit_date'].astype('datetime64[ns]')
        data['visit_date_added_holiday'] = \
            data['visit_date'].isin(add.russian_holidays)
        # числовые признаки сделаем строго положительными 
        # для лучшей обработки на шаге с YeoJohnsonTransformer
        data['visit_date_weekday'] = data['visit_date'].dt.weekday + 1
        data['visit_date_weekend'] = data['visit_date'].dt.weekday > 4
        data['visit_date_day'] = data['visit_date'].dt.day + 1

    # visit_time признаки
    if 'visit_time' in data.columns:
        data['visit_time'] = data['visit_time'].astype('datetime64[ns]')
        data['visit_time_hour'] = data['visit_time'].dt.hour + 1
        data['visit_time_minute'] = data['visit_time'].dt.minute + 1
        data['visit_time_night'] = data['visit_time'].dt.hour < 9

    # utm_* признаки
    if 'utm_medium' in data.columns:
        data['utm_medium_added_is_organic'] = \
            data['utm_medium'].isin(add.organic_mediums)
    if 'utm_source' in data.columns: 
        data['utm_source_added_is_social'] = \
            data['utm_source'].isin(add.social_media_sources)
    
    # device_screen признаки
    if 'device_screen_resolution' in data.columns:
        name = 'device_screen_resolution'
        data[[name + '_width', name + '_height']] = \
            data[name].str.split('x', expand=True).astype(float)
        data[name + '_area'] = data[name + '_width'] * data[name + '_height']
        data[name + '_ratio'] = data[name + '_width'] / data[name + '_height']
        data[name + '_ratio_greater_1'] = data[name + '_ratio'] > 1

    # geo_city признаки 
    if 'geo_city' in data.columns:
        data['geo_city_added_is_moscow_region'] = \
            data['geo_city'].isin(add.moscow_region_cities)
        data['geo_city_added_is_big'] = data['geo_city'].isin(add.big_cities)
        data['geo_city_is_big_or_in_moscow_region'] = \
            data['geo_city_added_is_moscow_region'] \
            | data['geo_city_added_is_big']
        data['geo_city_added_distance_from_moscow'] = \
            data['geo_city'].apply(add.get_distance_from_moscow)
        data['geo_city_added_distance_from_moscow_category'] = \
            data['geo_city_added_distance_from_moscow']\
                .apply(_distance_category)

    return data


def _distance_category(distance: float) -> str:
    """Возвращает категорию расстояния до Москвы."""

    if distance == -1: return 'no distance'
    elif distance == 0: return 'moscow'
    elif distance < 100: return '< 100 km'
    elif distance < 500: return '100-500 km'
    elif distance < 1000: return '500-1000 km'
    elif distance < 3000: return '1000-3000 km'
    else: return '>= 3000 km'


def _converse_types(data: pd.DataFrame) -> pd.DataFrame:
    """Приводит типы переменных к float. В первую очередь 
    необходимо для преобразования bool значений.
    """

    return data.astype(float)


def _get_metadata(model, X, y) -> _metadata_type:
    """Оцениваем модель и возвращает метаданные."""

    # Выделим тестовую часть и на ней оценим модель
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=200_000, stratify=y, random_state=RANDOM_SEED)
    
    # Обучим модель и получим лучший 
    # порог перевода вероятностей в классы
    model.fit(X_train, y_train)
    probas = model.predict_proba(X_test)[:, 1]
    threshold = _find_best_threshold(y_test, probas)

    return {
        'name': NAME, 
        'descripton': DESCRIPTION,  
        'version': VERSION, 
        'author': AUTHOR, 
        'model_type': model['model'].__class__.__name__,
        'training_datetime': str(datetime.now()), 
        'threshold': threshold, 
        'metrics': _get_metrics(y_test, probas, threshold)}


def _find_best_threshold(
    y_true: pd.Series, 
    y_proba: pd.Series, 
    iterations: int = 250, 
    learning_rate: float = 0.05
) -> float:
    """Находит лучший порог перевода вероятностей `y_proba` 
    в принадлежность к классу 1.
    """

    # Получение метрики
    def get_metric(threshold: float) -> float:
        prediction = (y_proba > threshold).astype(int)
        return roc_auc_score(y_true, prediction)

    direction = -1
    shift = 0.25

    best_threshold = 0.5
    best_metric = get_metric(best_threshold)

    # На каждой итерации
    for i in range(iterations):

        # Меняем порог
        threshold = best_threshold + direction * shift
        shift *= (1 - learning_rate)
        metric = get_metric(threshold)

        # И проверяем, улучшилась ли метрика
        if metric > best_metric: 
            best_threshold = threshold
            best_metric = metric
        else: 
            direction *= -1
            
    return best_threshold


def _get_metrics(y_true, y_proba, threshold) -> Dict[str, float]:
    """Возвращает метрики модели для заданных 
    вероятностей и порога их перевода в класс.
    """

    prediction = (y_proba > threshold).astype(float)

    return {
        'roc_auc': roc_auc_score(y_true, y_proba), 
        'roc_auc_by_class': roc_auc_score(y_true, prediction),
        'accuracy': accuracy_score(y_true, prediction), 
        'precision': precision_score(y_true, prediction), 
        'recall': recall_score(y_true, prediction), 
        'f1': f1_score(y_true, prediction)}


def _save_model(
    model: BaseEstimator, 
    metadata: _metadata_type, 
    folder: PathLike
) -> None:
    """Сохраняет модель с метаданными в папку с моделями."""
    
    folder = Path(folder)
    folder.mkdir(exist_ok=True)
    filename = f'model_{datetime.now():%Y%m%d%H%M%S}.pkl'

    model.metadata = metadata
    with open(folder / filename, 'wb') as file:
        dill.dump(model, file)


if __name__ == '__main__':
    create_model()
