class DivisioError(Exception):
    """Error en operacion"""


a = 0
b = 0
try:
    a = int(input("Digita un número"))
    b = int(input("Digita otr número"))
    if b == 2:
        raise Exception("No esta permitido el calculo por 2")
    resultado = a / b
except ValueError:
    print("El valor que digito no es un numero valido")
except ZeroDivisionError:
    print("No se puede dividir entre cero")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Desde finally")

print("Este es otro print")
