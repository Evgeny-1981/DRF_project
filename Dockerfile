FROM python:3.12-slim
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock .
RUN poetry install --no-root
COPY . .

#Убираем эту команду ниже, так как запуск будет производиться через docker compose

#CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver", "0.0.0.0:8000"]