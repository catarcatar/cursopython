''' Ejercicio 3

Escribe un programa que le pida al usuario ingresar un número, luego le pida un segundo número, e imprima en la consola la suma de los dos números que ingresó el usuario. '''
      
print("¿Cuántos minutos te demoras en llegar de tu casa al trabajo?")
minutos = int(input())
print("¿Cuántos días a la semana vas al trabajo?")
dias = int(input())
total = ((minutos * 2) * (dias * 4))/60
print("¿Sabías qué si trabajaras desde casa te ahorrarías " + str(total) + " horas al mes? ")