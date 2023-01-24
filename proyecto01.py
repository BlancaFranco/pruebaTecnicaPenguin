# Instrucciones

# Hacer un programa que juegue Piedra, papel o tijera, teniendo al usuario y
# la computadora como contrincantes


#Blanca Franco 23.01.2023
from random import randint #importamos esta funcion para generar numeros aleatorios
import math 


def jugar():
    
    opciones = ["piedra", "papel", "tijera"] #una lista de las posibles opciones
    
    turno_compu = opciones[randint(0,2)] #se genera un indice aleatorio entre 0-2 y se almacena en la variable un elemento de la lista
    turno_usuario = input( "\npiedra, papel, o tijera???: " ).lower() #convertimos directamente a miniscula por si se llega a ingresar en mayuscula 

    #validamos la opcion q se ingrese
    while True:
        if turno_usuario not in opciones:
            turno_usuario = input( "Error. Vuelva a ingresar\nOpciones: piedra, papel o tijera: " ).lower() 
        else:
            break

    if turno_usuario == turno_compu:
        return ( 0,turno_usuario,turno_compu ) #se retornara 0 si es un empate, y tambien las opciones de los jugadores
    elif ganador( turno_usuario, turno_compu ):
        return( 1,turno_usuario,turno_compu ) #se retornara 1 si gana el usuario y tambien las opciones de los jugadores
    else:
        return( -1,turno_usuario,turno_compu ) # #se retornara -1 si pierde el usuario, y tambien las opciones de los jugadores



def iniciar( cant_para_ganar,jugador ):
    detalle = "-" * 25
    
    cont_usuario = 0 #variable q va acumular la cantidad de veces q gana el usuario 
    cont_compu = 0 #variable q va acumular la cantidad de veces q gana la compu

    while cont_usuario < cant_para_ganar and cont_compu < cant_para_ganar:

        resultado, usuario, computadora = jugar()

        #empate
        if resultado == 0:
            print(f"""\n\t\t\t\U0001F634 EMPATE!
                    {jugador}: {usuario} -- Computadora: {computadora}""")
            print(f"\n\tMARCADOR\n{detalle}\n{jugador} -- Computadora\n{detalle}\n  {cont_usuario}\t--\t{cont_compu}\n")
        elif resultado == 1: #el usuario gana
            cont_usuario +=1 #se suma 1 a la variable que acumula los puntos del usuario
            print(f"""\n\t\t\t\U0001F60E GANASTE!
                {jugador}: {usuario} -- Computadora: {computadora}""" )
            print(f"\n\tMARCADOR\n{detalle}\n{jugador} -- Computadora\n{detalle}\n  {cont_usuario}\t--\t{cont_compu}\n")
        else: #gana la computadora
            cont_compu += 1 ##se suma 1 a la variable que acumula los puntos de la cumpu
            print(f"""\n\t\t\t\U0001F62A PERDISTE 
                {jugador}: {usuario} -- Computadora: {computadora}""")
            print(f"\n\tMARCADOR\n{detalle}\n{jugador} -- Computadora\n{detalle}\n  {cont_usuario}\t--\t{cont_compu}\n")
    
    if( cont_usuario > cont_compu ):
        print("\t\U0001F973 ¡¡GANASTE.FELICITACIONES!!\U0001F60E\n")
    else:
        print("\t\U0001F62A UPS!. Suerte para la proxima\n")
        


#funcion para saber si el usuario gana
def ganador( usuario, compu ):
    if( usuario == "piedra" and compu == "tijera" ) or ( usuario == "tijera" and compu == "papel" ) or ( usuario == "papel" and compu == "piedra" ):
        return True
    return False




partidas = int(input("\nIngrese la cantidad de rounds que desea jugar: "))
cantParaGanar = math.ceil( partidas/2 ) #usamos esta funcion para q retorne el número entero más pequeño que es mayor o igual que el argumento 
jugador = input( "\nIngrese tu nickname: " ) 

iniciar( cantParaGanar,jugador ) #llamamos a nuestra funcion principal para iniciar el juego