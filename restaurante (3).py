"""
Nombre :
Grupo :
Fecha :

Clase Restaurante con menu, reservaciones y manejo de ordenes
Escribe una clase llamada Restaurante con los atributos menu, agenda, y ordenes
Realizas las siguientes operaciones:
Agregar platillos al menu.
Tener la posibilidad de hacer reservaciones
Tomar las ordenes de los clientes.
Mostrar el mennu.
Mostrar el listado de reservaciones.
Mostrar las ordenes.
Utilizar diccionarios y listas para almacenar los datos.
"""
#Bienvenido a epstein island food
print("1 ensalada cesar")
print("2 spaghetti")
print("3 sopa de tomate")
print("4 Sopa de brocoli")
print("5 sopa de caracol")
menu=int(input("selecciona su platillo: "))
if menu==1:
  print("elegiste o seleccionaste el platillo 1")
elif menu==2:
  print("elegiste o seleccionaste el platillo 2")
elif menu==3:
  print("elegiste o seleccionaste el platillo 3")
elif menu==4:
  print("elegiste o seleccionaste el platillo 4")
elif menu==5:
  print("elegiste o seleccionaste el platillo 5")
else:
  print("aun en espera...")
  #bienvenido a las reservaciones  tiene reservacion....?
  print("1 tengo reservacion")
  print("2 vengo por una reservacion")
  print("3 no tengo reservacion")
reservacion=int(input("tengo...:"))
if reservacion==1:
  print("si tengo reservacion")
elif reservacion==2:
  print("vengo por una reservacion")
elif reservacion==3:
  print("no tengo reservacion")
else:
  print("tiene o no....?")
#menu de bebidas...
print("1 copa de champan")
print("2 copa de vodka")
print("3 copa de vino")
print("4 agua mineral")
print("5 jugo de frutas")
print("6 refresco de cola")
bebidas=int(input("elige tu bebida: "))
if bebidas==1:
  print("elegiste champan espera")
elif bebidas==2:
  print("elegiste copa de vodka espera")
elif bebidas==3:
  print("elegiste copa de vino espera")
elif bebidas==4:
  print("elegiste agua mineral espera")
elif bebidas==5:
  print("elegiste jugo de frutas espera")
elif bebidas==6:
  print("elegiste refresco coca cola espera")
else:
  print("aun en espera...")
"""
Resultado:
"""