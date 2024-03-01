FROM python:3.12-slim

# Empeche la générationd es fichiers .pyc dans le conteneur
ENV PYTHONDONTWRITEBYTECODE=1
# S'assure que les print() sois affichés instantanement dans le terminal
ENV PYTHONUNBUFFERED=1

ENV IN_DOCKER = 1

COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
# --dev pour installer les lib sous la balise [dev-packages] du Pipfile
# --system pour installer les lib dans le docker et non dans un env virtuel
# --deploy pour suivre le pipfile.Lock et ainsi s'assurer que les versions sont à jour et stables
RUN pip install pipenv && pipenv install --dev --system --deploy && pip list

WORKDIR /app
COPY . /app

EXPOSE 8000

ENTRYPOINT ["sh", "-c", "./scripts/start.sh"]