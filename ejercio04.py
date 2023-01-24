# Instrucciones

# Un número Armstrong es un número que es la suma de sus propios dígitos
# elevados cada uno a la potencia de la cantidad de dígitos.


# Por ejemplo:

# 9 es un número de Armstrong, porque 9 = 9^1 = 9
# 10 no es un número de Armstrong, porque 10 != 1^2 + 0^2 = 1
# 153 es un número de Armstrong, porque 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# 154 no es un número de Armstrong, porque: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

# Escribe algún código para determinar si un número es un número Armstrong.

#Blanca Franco 23.01.2023

def verificar_numero(numero): #se define la funcion de un parametro que va a verificar si el numero es o no un numero de Armstrong
    suma = 0 #acumulador
    for digito in numero:
        suma  +=  (int(digito) ** len(numero)) #se acumula la suma de los digitos del numero elevados a la potencia de la cantidad total de digitos
                                            #se convierte los digitos a un int para que se pueda realizar la suma 
    if suma == int(numero): #para realizar la comparacion era necesario convertir el numero al mismo tipo de dato que la variable suma
        return "Es un numero de Armstrong"
    else:
        return "NO un numero de Armstrong"

#entrada de dato
numero = input("Ingrese un numero: ")

#muestra en pantalla
print(verificar_numero(numero))
