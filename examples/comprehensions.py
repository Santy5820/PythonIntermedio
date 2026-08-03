from sample_data import sample_articles


def extract_title_traditional(articles):
    """Extrae todos los titulos usando un for"""
    titles = []
    for article in articles:
        titles.append(article["title"])
    return titles


def extract_titles(articles):
    """Extrae todos los titulos del dicc usando comprenhension"""
    return [article["title"] for article in articles]


def extract_article_summarie(articles):
    """Extrae del diccionario el titulo y la descripcion del articulo"""
    return {
        article["title"]: article["description"]
        for article in articles
        if len(article["description"]) > 5
    }


def extract_source(articles):
    """Extrae las fuentes de los articulos."""
    source = []
    for article in articles:
        if not article["source"]["name"] in source:
            source.append(article["source"]["name"])
        else:
            pass
    return source


def extract_source_comp(articles):
    """Extrae las fuentes sin repetir con comprehension"""
    return {article["source"]["name"] for article in articles}


def extract_source_platzi1(articles):
    sources = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources


def extract_source_platziComp(articles):
    return {
        article.get("source").get("name")
        for article in articles
        if article.get("source") and article.get("source").get("name")
    }


def categorize_traditional(articles):
    sources = extract_source_platziComp(articles)
    results = {}
    for source in sources:
        if source not in results:
            results[source] = []
        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)
    return results


def categorize(articles):
    sources = extract_source_platziComp(articles)
    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }


print(categorize(sample_articles))
