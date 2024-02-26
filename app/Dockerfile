FROM python:3.12-slim

LABEL version="alpha"

# Empeche la générationd es fichiers .pyc dans le conteneur
ENV PYTHONDONTWRITEBYTECODE=1
# Turns off buffering for easier container logging (?)
ENV PYTHONUNBUFFERED=1

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy

WORKDIR /app
COPY . /app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]