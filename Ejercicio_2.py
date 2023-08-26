"""
Crea un programa que pida al usuario ingresar dos números 
y luego muestre cuál de los dos es mayor.
"""

num1 = float(input("ingrese el primer número: ")) #es necesario determinar el tipo de dato, ya que sino no entra a las compraciones
num2 = float(input("ingrese el segundo número: "))

if num1 > num2:
    print(f"{num1} es mayor a {num2}")
elif num2 == num1:
    print("los números son iguales")
else:
    print(f"{num2} es mayor a {num1}")
