''' (Ejercicio 14

Escribe una función llamada mas_del_doble que reciba dos parámetros: num1 y num2. La función debe retornar True si num1 es más del doble de num2. De lo contrario debe retornar False.

# escribe la función mas_del_doble acá

# código de prueba
print(mas_del_doble(2, 5)) # True
print(mas_del_doble(5, 10)) # False '''

def mas_del_doble(num1,num2):
  if num1 > (num2*2):
    return True
  else:
    return False

print(mas_del_doble(20, 5)) # True
print(mas_del_doble(5, 10)) # False