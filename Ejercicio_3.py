"""
Escribe un programa que pida al usuario ingresar un número 
y determine si es positivo, negativo o cero.
"""

num = float(input("ingrese un número: "))

if num < 0:
    print("el número es negativo")
elif num > 0:
    print("el número es positivo")
else:
    print ("el número es 0")