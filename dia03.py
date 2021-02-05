#Retroalimentación
#Importar librerías 

''' def propina(total,porcentaje):
  total_tip=(total+porcentaje)/100
  return total_tip '''

#1.Condicionales o control de flujo 

''' print(1==1) #da true
print(2==1) #da false
print(1!=1)  #da false
print(2!=1) #da true
print("3"==3) #da false porque uno es string y el otro integer'''

#2.Expresiones booleanas
#True
#False

#3. Operadores relacionales u Operadores de comparación
#igual ==
#diferente !=
#mayor que >
#menor que <
#mayor o igual >=
#menor o igual <=

#4. Variables booleanas

''' var1=1
var2="hola"
var3=True

var4='3'
var5=3

print(var4==var5)  '''#compara variables

''' dado_a_false=False
dado_a_true=True
print(dado_a_false==dado_a_true)

bool_uno=5!=7
bool_dos=(1+1)!=2
bool_tres=(3*3)==9
print(bool_dos)  '''

#5. Sentencias if
''' if esta_lloviendo:
  llevar_sombrilla()

if 2==2:
  print("llevar sombrilla") ''' #solo imprime si el condicional se cumple

#condicional con la los valores almacenados en una variable

''' bool_cuatro=2==2
if bool_cuatro:
  print("Llevar sombrilla")  '''

#Ejemplo: Programa que chequee la edad para dejar ingresar a un programa
''' def verificar_edad(edad):
 if edad>=13:
  return True

print(verificar_edad(13)) #imprime true porque se cumple
print(verificar_edad(9)) #imprime none porque no se cumple'''

#6.Operaciones booleanas

# and
#print((1+1==2)and(2+2==4)) #las 2 son true entonces el resultado es true
#print((1+1==3)and(2+2==4)) #una es true otra es false el resultado es false '''

''' #or
print((1+1==3)or(2+2==4)) #una es true otra es false el resultado es true
print((1+1==3)or(2+2==5)) #las 2 son false entonces el resultado es false
 '''

#not

#print(not True==True)

#7.Sentencias else y elif
#else

''' def verificar_edad(edad):
 if edad>=13:
  return True
 else:
   return False #o también se puede return ("Usted no tiene la edad suficiente para acceder a este programa")

print(verificar_edad(8)) '''

# elif

''' def gracias(donacion):
 if donacion>=100000:
   print ("Gracias, su nivel es Diamante")
 elif donacion>=50000:
    print ("Gracias, su nivel es Oro")
 elif donacion>=10000:
    print ("Gracias, su nivel es Plata")
 else:
   print("Gracias, su nivel es Bronce")

gracias(80000) '''

#8.Sentencias else y elif con and 
''' 
def gracias(donacion):
 if donacion>=80000 and donacion<=100000:
 #se va ejacutando el que primero se cumpla
    print ("Gracias, su nivel es Diamante")
 elif donacion>=50000:
    print ("Gracias, su nivel es Oro")
 elif donacion>=10000:
    print ("Gracias, su nivel es Plata")
 else:
   print("Gracias, su nivel es Bronce")

gracias(90000) ''' 
