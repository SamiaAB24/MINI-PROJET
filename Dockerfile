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

# Démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#Vérifier la présence de manage.py
RUN ls -l /app/manage.py
