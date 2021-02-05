''' Ejercicio 15

Escribe una función llamada gran_exponente que reciba dos parámetros: base y exponente. Si base elevado a exponente es más de 5000 debe retornar True. De lo contrario debe retornar False '''
''' 
# escribe la función gran_exponente acá

# código de prueba
print(gran_exponente(2, 8)) # False
print(gran_exponente(5, 1000)) # False
print(gran_exponente(6, 900)) # True '''

def gran_exponente(base, exponente):
  if (base**exponente) > 5000:
    return True
  else:
    return False 

print(gran_exponente(2, 8)) # False
print(gran_exponente(5, 1000)) # False
print(gran_exponente(6, 900)) # True
