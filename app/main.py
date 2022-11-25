import logging

from fastapi import FastAPI

from .status import Status


# Создание логгера
log_format = '%(asctime)s %(levelname)s %(name)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger(__name__)

# Создание приложения
app = FastAPI()
status = Status.NO_MODEL
logger.debug(f'Приложение создано. Статус: {status.name}')


@app.get('/status')
def get_status() -> str:
    """Возвращает статус сервиса."""

    logger.debug(f'Запрос статуса сервиса. Статус: {status.name}')
    return status.value
