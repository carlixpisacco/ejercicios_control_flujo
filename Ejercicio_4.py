"""
Crea un programa que solicite al usuario ingresar una contraseña. 
Si la contraseña es "contraseña123", imprime "Acceso concedido". 
De lo contrario, imprime "Acceso denegado".
"""

contra = "contraseña123"
ingresada = input("ingrese la contraseña: ")
ingresada_minusculas= ingresada.lower() #convierto lo ingresado por el usuario a minusc
#sino simplemente comparo contra con ingresada, si pone mayus no son iguales y listo. 


if ingresada_minusculas == contra:
    print("acceso concecido")
else:
    print("acceso denegado")




