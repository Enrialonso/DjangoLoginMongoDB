# Django Login MongoDB
Sistema de registro y login sencillo basado en Django + persistencia con MongoDB (Djongo). Este es un primer acercamiento serio al Framework Django en su versión 2.0.2, usando como persistencia de datos MongoDB con Djongo una librería que traduce de las sentencias SQL generadas por el ORM de Django a el lenguaje propi a de MongoDB.
# Instalacion
- mkdir **nombre/de/la/carpeta**
- cd **nombre/de/la/carpeta**
- git clone **https://github.com/Enrialonso/DjangoLoginMongoDB.git**
- cd **DjangoLoginMongoDB**
- virtualenv **venv**
- source **venv/bin/activate** (linux) o **./venv/Scripts/activate.bat** (Windows)
- pip **install** -r **requirements.txt**
_________________________________________________________________________________________
- Como requisito debes tener instalado y corriendo MongoDB y tener creada la DB **"djangologinmongo"** en la instancia antes de seguir con los comando.
________________________________________________________________________________________
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

Abrimos el navegador en la siguiente url: **http://localhost:8000*
