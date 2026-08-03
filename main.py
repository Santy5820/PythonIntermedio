# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

# PEP 8: Configuración centralizada - constantes en MAYÚSCULA con guiones bajos
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LANGUAGE = "es"  # PEP 8: Comillas dobles para strings


# PEP 8: Utilidades comunes del proyecto - funciones en snake_case
def clean_text(text):
    # PEP 8: 4 espacios por indentación, no tabs
    """Limpia y normaliza un texto de entrada.

    Elimina los espacios en blanco al inicio y al final de la cadena,
    y convierte todos los caracteres a minúsculas. Si el texto de
    entrada es vacío, None o cualquier valor "falsy", devuelve una
    cadena vacía en su lugar.

    Args:
        text (str): Cadena de texto a limpiar y normalizar. Puede ser
            None o una cadena vacía.

    Returns:
        str: El texto normalizado (sin espacios en los extremos y en
            minúsculas). Devuelve una cadena vacía ("") si `text` es
            None, vacío o "falsy".

    Raises:
        AttributeError: Si `text` no es None/vacío pero tampoco es
            una cadena (por ejemplo, un entero o una lista), ya que
            dichos tipos no cuentan con los métodos `strip()` y
            `lower()`.

    Example:
        >>> clean_text("  Hola MUNDO  ")
        'hola mundo'
        >>> clean_text("")
        ''
        >>> clean_text(None)
        ''
    """
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble linea en blanco entre funciones para separar logicamente
def validate_pi_key(api_key):
    """Valida que la API key tenga un formato correcto."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas despues de utilidades
def fetch_news_from_api(api_name, query):
    """Obtiene noticias de una API especifica"""


def process_article_data(raw_data):
    """Procesa datos crudos de articulo"""


# Longitud de línea: Máximo 88 caracteres (Ruff default)
# Indentación: 4 espacios, nunca tabs
# Nombres descriptivos: snake_case para funciones y variables
# Imports ordenados: estándar → terceros → locales
# Líneas en blanco: Separar funciones y clases lógicamente
# Comillas consistentes: Usar comillas dobles para strings


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def ejemplo_args(api_key, *args):
    print(f"api_key: {api_key}")
    print(f"Imprimir todos los args {args}")
    print(f"type args: {type(args)}")


def ejemplo_kwargs(**kwargs):
    print(f"kwargs: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("======")


# ejemplo_kwargs(api_key="DEMO", query="Noticioas de Python", timeout=30, retries=3)

import json
import os
import urllib.parse
import urllib.request

from dotenv import load_dotenv

load_dotenv()  # Cargar variables de entorno desde .env

API_KEY = os.getenv("NEWS_API_KEY")  # Obtener la API Key desde la variable de entorno
BASE_URL = "https://newsapi.org/v2/everything"


class NewsSystemError(Exception):
    """Error general en la app"""


class APIKeyError(NewsSystemError):
    """Error en la API Key"""


def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.URLError:
        raise APIKeyError("Ocurrio un error no se pudo contactar con la API")
    return f"NewsAPI:{query} con timeout {timeout}"


def fetch_news(api_name, *args, **kwargs):
    """Funcion flexible para conectar con la API"""
    base_config = {"timeout": 30, "retries": 3}
    config = {
        **base_config,
        **kwargs,
    }
    api_clients = {
        "newapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)


response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"Error en la API Key: {e}")
if response_data:
    for article in response_data["articles"]:
        print(article["title"])
