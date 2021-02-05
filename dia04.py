''' ##Listas
alturas = ([1.9, 1.7, 1.5, 1.2, 1.3]) #floats o integers
nombres = ["Ana", "Andrea", "Juan", "Pedro", "Julian"] #strings
mix = [12, "Juan", True] #numeros, strings o booleans
lista_lista = [["Ana", 1.6]]
lista_vacia = []

print(alturas)
print(nombres)
print()
print(lista_vacia)

lista_vacia.append(1) #llena una lista, agrega solo un valor
print(lista_vacia)

lista_vacia.append([1,2]) #agrega dos valores sirve pero no es tan útil


lista_vacia+([2,3,"Ana"])

lista_vacia = lista_vacia+([2,3,"Ana"]) #agregar valorescon el signo +
print(lista_vacia)

lista_con_valores = [2,3,"Ana"]
lista_vacia = lista_vacia + lista_con_valores

lista_vacia += lista_con_valores #refatorización += para concatenación de valores con la suma

#Ïndice de las listas
alturas = ([1.9, 1.7, 1.5, 1.2, 1.3]) #pyton indexa desde cero, les da una posición 1.9 es posición 0, 1.7 es posición 1, etc. Esto sirve para seleccionar un elemento de la lista. 

#cambiar un valor
alturas[1] = 2 


#Insertar
alturas.insert()

#Eliminar un elemento
# con pop
alturas.pop(0) #elimina un elemento de la posición deseada
alturas.pop() #elimina el ultimo elemento

#con del 
del alturas #elimina toda la variable y con ello toda la lista. da NameError

# con clear
alturas.clear() #vaciar la lista sin eliminarla

## Seleccionar elementos
#Basado en el indice
print(alturas[-1]) #selecciona el ultimo elemento si se usa - selecciona el penúltimo, -3 el antepenúltimo y asi sucesivamente.

#Slicing lists
#Por pedazos
letras = ["a", "b", "c", "d", "e", "f", "g"]

#letras[indice]
##### #letras [inicio:fin] desde esta posición hasta la otra posición
# fin = valor - 1 (para encontrar el valor desde el final)

#seleccionar de b hasattr
sublista = letras[1:6]

#fin = indice + 1 (para encontrar el valor desde el principio) 

print(letras[0:3]) #trae a,b,c

print(letras[:3]) #sirve si se elimina el cero porque python simepre arranca desde cero

print(letras[2:])#selecciona desde la posción 2 hasta el final sin especificar cual es final

print(letras[-3:]) #e, f y g trae el trozo desde la posción -3 hasta el final

print(letras[:-3]) #trae a, b, c y d pero no trae e porque el fin siempre es -1 como dice en la línea 59 '''


##Range

mi_rango = range (10) #desde 0 hasta 9
print(list(mi_rango)) #se debe hacer conversion de tipos se hace al decir que mi rango es una lista

mi_rango = range (2,10) #desde 2 hasta 9
print(list(mi_rango))
#se cambia si uno quiere cambiar el número inicial

mi_rango = range (2,10,2) #desde 2 hasta 8 porque le resta 2 al final
print(list(mi_rango))
#si uno quiere que haga saltos

#len
mi_rango = range (10) 
mi_rango_list = list(mi_rango)

print(list(mi_rango))
print(len(mi_rango_list))

#zip
#emparejar 2 listas
#alturas con nombres (deben tener la misma cantidad de elementos) los empareja por posición 
alturas = ([1.9, 1.7, 1.5, 1.2, 1.3]) #floats o integers
nombres = ["Ana", "Andrea", "Juan", "Pedro", "Julian"]
print((zip(alturas, nombres))

print(list(zip(alturas, nombres)))
#al poner el list imprime los nombres y no las posiciones