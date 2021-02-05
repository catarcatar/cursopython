''' Ejercicio 5

El área de un rectángulo se calcula con la siguiente fórmula:

base * altura

Escribe un programa que le pida al usuario la base y la altura de un rectángulo, e imprima la frase "El área es " seguido del área calculada. Por ejemplo:

Ingresa la base del rectángulo: 5
Ingresa la altura del rectángulo: 10

El área es 50 '''

print("Este programa calcula el área de un rectángulo \n¿Cuál es medida de la base del rectángulo en cm?")
base = int(input())
print("¿Cuál es medida de la altura del rectángulo en cm?")
altura = int(input())
area = base * altura
print("El área del rectángulo es " + str(area) + " cm2.")