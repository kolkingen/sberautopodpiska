import logging

import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from .status import Status
from .loader import load_model
from .metadata import Metadata
from .prediction import Prediction
from .data_form import DataForm


# Создание логгера
log_format = '%(asctime)s %(levelname)s %(name)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger(__name__)

# Создание приложения
app = FastAPI()
status = Status.NO_MODEL
model = None
logger.debug(f'Приложение создано. Статус: {status.name}.')


@app.get('/status')
def get_status() -> str:
    """Возвращает статус сервиса."""

    logger.debug(f'Запрос статуса сервиса. Статус: {status.name}.')
    return status.value


def _check_status() -> None:
    """Проверяет статус сервиса. Если он не работает вызывает ошибку."""

    if status != Status.OK:
        logger.error(
            f'Запрос не может быть выполнен, сервис не готов к работе.')
        raise HTTPException(status_code=404, detail=status.value)


@app.get('/version', response_model=Metadata)
def get_metadata() -> Metadata:
    """Возвращает метаданные модели."""

    logger.debug(f'Запрос метаданных модели. Статус: {status.name}.')
    _check_status()
    try: 
        metadata = model.metadata
    except AttributeError:
        logger.error(f'Запрос метаданных отклонён: у модели нет метаданных.')
        raise HTTPException(status_code=404, detail='У модели нет метаданных.')
    else:
        return Metadata.parse_obj(metadata)


def _predict(data: pd.DataFrame, return_proba: bool = False) -> pd.Series:
    """Предсказывает класс или вероятность положительного класса."""

    # Получаем порог
    try: 
        threshold = model.metadata['threshold']
    except:
        threshold = 0.5

    # Производим предсказание 
    try: 
        prediction = model.predict_proba(data)[:, 1]
    except AttributeError:
        prediction = model.predict(data)
    else:
        if not return_proba:
            prediction = (prediction > threshold).astype(float)

    return prediction


@app.post('/predict', response_model=Prediction)
def predict_class(data_form: DataForm) -> Prediction:
    """Возвращает предсказанный класс."""

    logger.debug(f'Запрос на предсказание класса. Статус: {status.name}.')
    _check_status()

    # Получение предсказания
    data = pd.DataFrame(jsonable_encoder([data_form]))
    prediction = _predict(data, return_proba=False)[0]
    logger.info(f'{prediction} - предсказание для '
                f'`sessions_id`={data_form.session_id}.')

    return Prediction(session_id=data_form.session_id, prediction=prediction)


@app.post('/predict_proba', response_model=Prediction)
def predict_proba(data_form: DataForm) -> Prediction:
    """Возвращает вероятность положительного класса."""

    logger.debug(f'Запрос на предсказание вероятности положительного класса. '
                 f'Статус: {status.name}.')
    _check_status()

    # Получение предсказания
    data = pd.DataFrame(jsonable_encoder([data_form]))
    prediction = _predict(data, return_proba=True)[0]
    logger.info(f'{prediction} - предсказание для '
                f'`sessions_id`={data_form.session_id}.')

    return Prediction(session_id=data_form.session_id, prediction=prediction)


# Загрузка модели
try:
    model = load_model('models')
except FileNotFoundError:
    status = Status.MODEL_ERROR
    logger.error(
        f'Невозможно загрузить модель. Статус: {status.name}.', exc_info=True)
except Exception:
    status = Status.ERROR
    logger.error(
        f'Невозможно загрузить модель. Статус: {status.name}.', exc_info=True)
else:
    status = Status.OK
    logger.debug(f'Модель загружена. Статус: {status.name}.')
