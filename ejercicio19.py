# Escribe una función crear_rango que reciba un número y retorne una lista desde 1 hasta el número recibido. Si el número es menor a 1 retorna un lista vacía.

# escribe la función crear_rango acá
def crear_rango(num):
  num+=1
  mi_rango=range(1,num)
  lista=list(mi_rango)
  return lista[:num-1]
  if num < 1:
    return lista

# código de prueba
print(crear_rango(5)) # [1, 2, 3, 4, 5]
print(crear_rango(1)) # [1]
print(crear_rango(0)) # []
print(crear_rango(-10)) # []


