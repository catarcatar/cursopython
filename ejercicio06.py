''' Ejercicio 6

Escriba una función llamada suma()que reciba dos números y retorne la suma de los dos números.

# escribe la función suma acá

# código de prueba, verifica que aparezcan los valores correctos en la consola
print(suma(1, 2)) # 3
print(suma(0, 0)) # 0
print(suma(245, 923)) # 1168 '''

def suma(a,b):
  return a+b
print(f'la suma de a + b es: {suma(1,2)}')
print("la suma de a + b es: {}".format(suma(0,0)))
print("la suma de a + b es: {}".format(suma(245,923)))