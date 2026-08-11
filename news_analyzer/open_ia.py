"""Configuracion de la IA"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Cargar variables de entorno desde .env


def analyze_news_with_ia(articles: list[dict], query: str) -> str | None:

    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    context = "\n".join(
        [
            f"- {article['title']}: {article.get('description', '')[:100]}..."
            for article in articles[:10]
        ]
    )

    prompt = f"""
        Basandote en estas noticias:
        {context}
        Pregunta: {query}
        Responde de forma concisa en español.
    """
    response = client.responses.create(
        model="gpt-5.5",
        instructions="Eres un agente que lee un contexto y responde brevemente",
        input=prompt,
    )

    return response.output_text
