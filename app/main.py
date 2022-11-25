import logging

from fastapi import FastAPI

from .status import Status
from .loader import load_model


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
