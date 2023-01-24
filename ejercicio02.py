# Instrucciones

# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase, seguido
# del porcentaje de veces que aparecela frase y el **porcentaje** de veces que aparece
# la letra en la frase.

#creamos una funcion con dos parametros q retornara la cantidad de repeticiones
def cant_repeticiones(letra, frase):
    cont = 0 #esta variable acumula la cantidad de repeticiones
    for i in frase:
        if i == letra:
            cont +=1
    return cont

#datos de entrada
frase = input("\nIngrese una frase: ")
letra = input("ingrese una letra: ")

cantRepeticiones = cant_repeticiones(letra, frase) #en la variable se guarda lo que retorna nuestra funcion que tiene como argumento la letra y la frase q se ingreso

porcentajeLetra = cantRepeticiones/len(frase) * 100 #se calcula el porcentaje de veces q aparece la letra en la frase y se guarda en la variable porcentajeLetra

#por ultimo se muestra en pantalla
print(f"\nla letra {letra} aparece {cantRepeticiones} veces en la frase, forma el {porcentajeLetra:.2f}% de la frase\n")




