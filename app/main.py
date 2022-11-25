import logging

from fastapi import FastAPI, HTTPException

from .status import Status
from .loader import load_model
from .metadata import Metadata


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
