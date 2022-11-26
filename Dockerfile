FROM python:3.9

# Создание рабочей папки и установка библиотек
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Копирование файлов проекта
COPY ./app /code/app
COPY ./create_model.py /code/create_model.py
COPY ./additional_data.py /code/additional_data.py

# Запуск сервера с приложением
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
