# Ejercicio 23
# Escribe una función llamada ultimo que reciba una lista y retorne el último elemento. Si la lista es vacía debe retornar "La lista está vacía":

#escribe la función ultimo acá
def ultimo(lista):
  cantidad=len(lista)
  if cantidad==0:
    return("La lista está vacía")
  else: return lista[-1]

# código de prueba
print(ultimo([3, 2, 1])) # 1
print(ultimo([5, 1, 8, 7])) # 7
print(ultimo([])) # "La lista está vacía"

# lista =[]
# cant_lista=len(lista)
# print(cant_lista)

# def nombre(num1,num2):
#   return num1+num2

# suma=nombre(2,3)
# print(suma)

# suma2=nombre(15,45)
# print(suma2)



