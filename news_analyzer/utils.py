"""Utilidades varias para la aplicación."""


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


def process_article_data(raw_data: dict) -> dict:
    """
    Procesa datos crudos de artículo.
    Args:
        raw_data (dict): Diccionario con datos crudos del artículo. Se espera que
                         contenga las claves 'title', 'author' y 'content'.
    Returns:
        dict: Diccionario con datos procesados y normalizados del artículo.
    """
    return {}


def get_unique_sources(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def get_articles_by_source(articles: list[dict], source: str) -> list[dict]:
    return list(
        filter(
            lambda article: article["source"]["name"].lower() == source.lower(),
            articles,
        )
    )


def get_reading_time(article: dict) -> dict:
    """Calcula el tiempo de lectura"""
    minutes = len(article["content"]) // 200 + 1
    article["reading_time"] = minutes
    return article
