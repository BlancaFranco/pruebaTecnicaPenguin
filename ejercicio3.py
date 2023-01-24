# Instrucciones

#Crear una funcion para validacion de nombres de usuarios.
#Dicha función deberá validar lo siguiente:

# - El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
# - El nombre de usuario debe ser alfanumérico.
# - Nombre de usuario con menos de 6 caracteres, retorna el mensaje 'El nombre de usuario debe contener al
# menos 6 caracteres'.
# - Nombre de usuario con más de 12 caracteres, retorna el mensaje 'El nombre de usuario no puede contener
# más de 12 caracteres'.
# - Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje 'El nombre de usuario
# puede contener solo letras y números'.
# - Nombre de usuario válido, retorna '¡Correcto!'

#Blanca Franco 23.01.2023

def validacion_usuario (usuario): #se crea la funcion con un parametro
    tipo = usuario.isalnum() #la variable "tipo" almacena un valor booleano, la funcion isalnum() verifica si es un dato alfanumerico
    #se realiza las respectivas validaciones
    if tipo:
        if len(usuario) < 6:
            return "El nombre de usuario debe contener al menos 6 caracteres"
        elif len(usuario) > 12:
            return "El nombre de usuario no puede contener más de 12 caracteres"
        else:
            return "¡Correcto!"
    else:
        return "El nombre de usuario puede contener solo letras y números"

#dato de entrada
usuario = input("\nIngrese nombre de usuario: ")

#se muestra en pantalla lo que retorna la funcion que tiene como argumento el nombre de usuario
print(validacion_usuario(usuario), "\n")

