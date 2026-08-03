# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.exceptions import APIKeyError

response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"Error en la API Key: {e}")
if response_data:
    print(f"response_data: {response_data}")
