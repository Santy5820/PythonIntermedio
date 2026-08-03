"""
Explicaicion de docstrings y comentarios en Python.

En esta clase vemow como funcionan los docstrings en Python

"""


def ejemplo_sin_docstring():
    return "Hola, Mundo!"


def ejemplo_con_docstring() -> str:
    """
    DESCRIPTION
    ARGS
    RETURNS
    EXCEPTIONS
    EXAMPLE

    Returns:
        str: Un saludo en español

    """

    return "Hola, Mundo!"


# print(ejemplo_con_docstring.__doc__)
# help(ejemplo_con_docstring)
print(ejemplo_sin_docstring.__doc__)
