import string
import getpass
# se utiliza getpass para que no se vean los caracteres mientras se escriben. 
contra_ingresada = getpass.getpass("ingrese la contraseña que solo deben ser letras: ")

# contra_minuscula es la variable que contiene el valor o nombre de la clave que se va a comparar con las letras del alfabeto
contra_minusculas = contra_ingresada.lower()
# la variable contador irá sumando cada intento por lo que se debe definir el valor inicial como iun número 0
contador = 0
# La sentencia string.ascii_lowercase hace aparecer el listado de letras de la a a la z sin la ñ, que se utilizará para buscar una a una las letras
alfabeto = string.ascii_lowercase

for contra in contra_minusculas:
    for caracter_alfabeto in alfabeto:
        contador += 1
        # si la letra coincide con el alfabeto corta el bucle y vuelve al primer for.
        if contra == caracter_alfabeto:
            
            break

print(f"La contraseña fue forzada en {contador} intetos")