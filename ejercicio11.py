''' Dicen que un año en un humano es equivalente a 7 años de vida de los perros. Escribe una función llamada edad_perruna que reciba dos parámetros: nombre y edad. La función debe calcular la edad en años perrunos y retornar la siguiente cadena de texto (string): ", tienes en años perrunos!".

# escribe la función edad_perruna acá

# código de prueba
print(edad_perruna("Pedro", 20)) # 140
print(edad_perruna("Maria", 8)) # 56
print(edad_perruna("Alex", 45)) # 315 '''

def edad_perruna(nombre,edad):
  calculo=edad*7
  return nombre+", tienes  "+str(calculo)+" años perrunos!"
print(edad_perruna("Pedro", 20)) # 140
print(edad_perruna("Maria", 8)) # 56
print(edad_perruna("Alex", 45)) # 315

#interpolacion
def edad_perruna(nombre,edad):
  calculo=edad*7
  return nombre+", tienes  "+str(calculo)+" años perrunos!"

#print(f'Tienes:{edad} años')
print(edad_perruna("Pedro", 20)) # 140
print(edad_perruna("Maria", 8)) # 56
print(edad_perruna("Alex", 45)) # 315