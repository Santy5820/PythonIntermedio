class NewsSystemError(Exception):
    """Error general en la app"""


class APIKeyError(NewsSystemError):
    """Error en la API Key"""
