# Ejercicio 21

# Escribe una función llamada combinar que reciba dos listas y retorne una nueva lista con los elementos combinados en tuplas:

# escribe la función combinar acá
def combinar(lista1,lista2):
  new_lista =list(zip(lista1,lista2))
  return new_lista

# código de prueba
print(combinar([1, 2], ['a', 'b'])) # [(1, 'a'), (2, 'b')]
print(combinar(["Pedro", "Maria"], [15, 22])) # [("Pedro", 15), ("Maria", 22)]

# lista1=["Pedro", "Maria","catalina","juan"]
# for listaA in range(len(lista1)):
#   print(lista1[listaA])

# for n in range(11):
#     print(n)

