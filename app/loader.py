from os import PathLike
from pathlib import Path
import logging

import dill
from sklearn.base import BaseEstimator


# Создание логгера
logger = logging.getLogger(__name__)

# Шаблон названия моделей
model_name_pattern = 'model_*.pkl'


def load_model(folder: PathLike) -> BaseEstimator:
    """Загружает последнюю модель из заданной папки."""

    # Получим список моделей в папке
    folder = Path(folder)
    model_files = list(folder.glob(model_name_pattern))
    logger.debug(f'Загрузка модели из папки {folder}.')

    # Если модели есть, загрузим послендюю
    if model_files:
        last_model = sorted(model_files)[-1]
        logger.debug(f'Загружается модель {last_model}.')
        with open(last_model, 'rb') as file:
            model = dill.load(file)
        return model
    
    # Иначе вызовем ошибку
    else:
        raise FileNotFoundError('Нет моделей в указанной папке.')
