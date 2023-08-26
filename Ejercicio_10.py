"""
Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número 
hasta cero separados por comas.
"""

num=int(input("ingrese un número entero positivo "))

for i in range(num,-1,-1):
    print(i, end=",") #end = "" permite separar lo que imprimo por un simbolo en este caso ",", el predeterminado es el salto de linea \n