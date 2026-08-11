# main.py - Todo el código en un archivo
"""
Sistema de análisis de noticias con APIs múltiples.
"""

from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.exceptions import APIKeyError
from news_analyzer.utils import (
    get_articles_by_source,
    get_reading_time,
    get_unique_sources,
)

response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"Error en la API Key: {e}")
if response_data:
    sources_set = get_unique_sources(response_data["articles"])
    for index, source in enumerate(sources_set, start=1):
        print(f"No. {index}. {source}")
    print(sources_set)
    articles = list(map(get_reading_time, response_data["articles"]))
    for art in articles:
        print(f"{art['title']} --- tiempo de lectura {art['reading_time']}")

    # for article in response_data["articles"]:
    #    print(article["title"])
    git_hub_articles = get_articles_by_source(response_data["articles"], "github.io")
    print("===================")
    print(git_hub_articles)
