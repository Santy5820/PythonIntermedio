import json
import urllib
import urllib.parse
import urllib.request
from collections.abc import Callable

from .config import BASE_URL
from .exceptions import APIKeyError


def validate_api_key(api_key: str) -> bool:
    """
    Valida que la API key tenga un formato correcto.

    Args:
        api_key (str): La clave de la API a validar.

    Returns:
        bool: True si la clave es válida, False en caso contrario.

    """
    return len(api_key) > 10 and api_key.isalnum()


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    """
    Cliente para la API de Guardian.
    Args:
        api_key (str): La clave de la API.
        section (str): La sección de noticias a consultar.
        from_date (str): La fecha desde la cual obtener noticias.
        timeout (int, optional): Tiempo de espera para la solicitud. Por defecto es 30 segundos.
        retries (int, optional): Número de reintentos en caso de fallo. Por defecto es 3.
    Raises:
    APIKeyError: Si ocurre un error al contactar con la API.
    Returns:
        str: Mensaje indicando la sección y fecha consultadas.
    """
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def newsapi_client(api_key, query, timeout=30, retries=3):
    """
    Cliente para la API de NewsAPI.
    Args:
        api_key (str): La clave de la API.
        query (str): La consulta de noticias a realizar.
        timeout (int, optional): Tiempo de espera para la solicitud. Por defecto es 30 segundos.
        retries (int, optional): Número de reintentos en caso de fallo. Por defecto es 3.
    Raises:
        APIKeyError: Si ocurre un error al contactar con la API.
    Returns:
        dict: Datos de respuestas en formato JSON.
    """
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrio un error no se pudo contactar con la API")
    return f"NewsAPI:{query} con timeout {timeout}"


def fetch_news(api_name, *args: tuple, **kwargs: dict) -> dict:
    """
    Funcion que recibe nombre de la API y argumentos para llamar al cliente correspondiente.
    Args:
        api_name (str): Nombre de la API a utilizar(newapi o guardian).
    """
    if api_name not in ("newapi", "guardian"):
        raise ValueError(f"API desconocida: {api_name}. Use 'newapi' o 'guardian'.")
    base_config = {"timeout": 30, "retries": 3}
    config = {
        **base_config,
        **kwargs,
    }
    api_clients: dict[str, Callable] = {
        "newapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)
