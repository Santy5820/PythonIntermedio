"""Configuracion de la aplicacion"""

import os

from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env

API_KEY = os.getenv("NEWS_API_KEY")  # Obtener la API Key desde la variable de entorno
BASE_URL = "https://newsapi.org/v2/everything"
