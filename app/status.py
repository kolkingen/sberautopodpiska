from enum import Enum


class Status(Enum):
    """Различные статусы сервиса."""

    OK = 'Сервис работает.'
    NO_MODEL = 'Модель ещё не загружена, повторите попытку позже.'
    MODEL_ERROR = 'Невозможно загрузить модель.'
    ERROR = 'Непредвиденная ошибка.'