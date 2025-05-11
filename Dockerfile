# Utiliser une image Python officielle
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier le code source
COPY . /app/

CMD ["sh", "-c", "python manage.py migrate && gunicorn MarketGo.wsgi:application --bind 0.0.0.0:8000"]
#ancer les migrations de la base de données avant de démarrer le serveur.
CMD ["sh", "-c", "python manage.py migrate && gunicorn MarketGo.wsgi:application --bind 0.0.0.0:8000"]


# Démarrer le serveur Django
CMD ["gunicorn", "MarketGo.wsgi:application", "--bind", "0.0.0.0:8000"]
