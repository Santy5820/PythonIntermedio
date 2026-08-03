name = "Ana"
year = 2020
text = f"Hola {name}"
text2 = "Hola"
print(text)

text_calculo = f"Hola,{name}, tu edad es: {2026 - year} años"
print(text_calculo)

text_func = f"HOLA {name.upper()}"
print(text_func)

edad = 20
text_if = f"Hola, {name}, eres {'mayor' if edad >= 18 else 'menor'} de edad"
print(text_if)


bank_balance = 1200000000
text3 = f"Tu salso en la cuenta bancaria es: {bank_balance:,}"
print(text3)

stock_price = 1.405
text4 = f"El valos del stock es de {stock_price:.1f}"
print(text4)

user_id = 1
text = f"Su id es: {user_id:04d}"
print(text)

product = "Laptop"
price = 1000

text = f"Producto: {product:<15} | Precio: {price:>10}"
print(text)
print(f"{text}\n{text}")


from datetime import datetime

date = datetime(2024, 12, 5, 10, 10)
text = f"La fecha completa es {date: %A %d de %B de %Y a las %I:%M %p}"
print(text)
