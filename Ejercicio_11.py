"""
 Escribir un programa que almacene la cadena de caracteres contraseña 
 en una variable, pregunte al usuario por la contraseña 
 hasta que introduzca la contraseña correcta.
 """

contra="contraseña"
contra_ingresada=input("ingrese la contraseña ")

while contra_ingresada != contra:
    contra_ingresada = input("contraseña inválida, por favor vuelva a ingresarla ")
    
   
