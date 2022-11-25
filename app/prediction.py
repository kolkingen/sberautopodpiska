from pydantic import BaseModel


class Prediction(BaseModel):
    """Структура отдельного предсказания модели. `prediction` может быть 
    как классом (0 или 1), так и вероятностью положительного класса.
    """

    session_id: str
    prediction: float
