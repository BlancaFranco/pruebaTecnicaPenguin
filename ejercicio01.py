#Instrucciones

#Los estudiantes consultan la nota que recibirán según las calificaciones que adquirieron

#Por ejemplo:

#Las valoraciones 4, 5, 3. Darán la nota 4
#Las valoraciones 3, 2, 5. Darán la nota 3.33

#Escribe algun codigo para determinar la nota de un estudiante

#Blanca Franco 23.01.2023

#Primeramente se le pedira al estudiante la cant de calificaciones 
cantCalif = int(input("Ingrese cantidad de calificaciones: "))
sumaCalif = 0 #variable que guardara la suma de las calificaciones

#en este bucle se va a ingresar las calificaciones y se van a sumar dichas calificaciones 
#el ciclo se repetira cuantas veces haya decidido el usuario
for i in range (cantCalif):
    calif = int(input(f"Ingrese calificacion nro{i+1}: "))
    sumaCalif += calif

nota = float(sumaCalif/cantCalif) #se calcula el promedio para sacar la nota y se convierte a un tipo de dato real

print(f"NOTA: {nota:.2f}") #se le muestra al usuario su nota final
