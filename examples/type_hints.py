"""Typing con Python"""

variable = 42  # int
print(f"variable: {variable} de tipo: {type(variable)}")
# variable = "Texto de prueba"  # str
print(f"variable: {variable} de tipo: {type(variable)}")

otra_variable: int = 42
print(f"otra_variable: {otra_variable} de tipo: {type(otra_variable)}")
# otra_variable = "Texto de prueba"

user_id: int | None = None


def suma_clara(a: int, b: int) -> int:
    return a + b


articles: list[dict] = [{"title": "Example"}, {"title": "Example 2"}]

# articles_dos: list[list[str]] = [["articulos", "otros", 123], ["articulos", "otros"]]
from typing import Any

articles_tres: list[list[Any]] = [["articulos", "otros", 123], ["articulos", "otros"]]
