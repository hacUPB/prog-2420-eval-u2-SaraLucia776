import random 
from datetime import datetime

from random import randint
def main():
   distancia = 0 
   costo = 0
   ciudades = ['Medellín', 'Bogotá', 'Cartagena']
   dias = ['Lunes','Martes','Miércoles', 'Jueves','Viernes','Sábado','Domingo']
   
   título = input("Ingrese su título (Sr o Sra) ").capitalize()
   nombre_completo = input("Ingrese su nombre completo: ")
   
   if título == ("Sr"):
     print(f"{título} {nombre_completo} Bienvenido a Sky Airlines")
   elif título == ("Sra"):
     print(f"{título}{nombre_completo} Bienvenido a Sky Airlines")
   
   origen = (input("Ingrese la ciudad de origen (Medellín, Bogotá, Cartagena)"))
   while True:
      if origen not in ciudades: 
         print("Ciudad de origen incorrecta, seleccione nuevamente")
         origen = (input("Ingrese la ciudad de origen (Medellín, Bogotá, Cartagena)"))
      else:
         break
   
   destino = (input("Ingrese la ciudad de destino (Medellín, Bogotá, Cartagena ) "))
   while True:
      if destino not in ciudades: 
         print("Ciudad de destino incorrecta, seleccione nuevamente")
         destino = (input("Ingrese la ciudad de destino (Medellín, Bogotá, Cartagena ) "))
      else:
         break 
   
   if  origen == ciudades[0] and destino == ciudades[1]:
      distancia == 240
   elif origen == ciudades[1] and destino == ciudades[0]:
      distancia == 240 
   elif origen == ciudades[0] and destino == ciudades[2]:
      distancia == 461 
   elif origen == ciudades[2] and destino == ciudades [0]:
      distancia == 461 
   elif origen == ciudades[1] and destino == ciudades[2]:
      destino == 657
   elif origen == ciudades[2] and destino == ciudades[1]:
      destino == 657
   else: 
      print("Viaje inválido")
   
   ***num_sem = int(input("Ingrese el día de la semana en el que viajará: \nLunes(1) \nMartes(2) \nMiércoles(3) \nJueves(4) \nViernes(5) \nSábado(6) \nDomingo(7): "))
   num_dia = int(input("Ingrese el día del mes en el que viajará "))
   num_mes = int(input("Ingrese el número del mes en el que viajará "))
   if num_sem <= 4 and distancia < 400: 
     costo = 79900
   elif num_sem > 4 and distancia < 400:
      costo = 119900
   elif num_sem <= 4 and distancia > 400:
      costo = 156900
   elif num_sem > 4 and distancia > 400:
      precio = 213000
   
   asientos = ['A', 'B', 'C']
   asiento = (input("Ingrese el asiento de su preferencia (Ventana, Sin preferencia, Pasillo)"))
   if asiento == "Ventana":
      asiento = 'A'
   elif asiento == "Sin preferencia":
      asiento = 'B' 
   elif asiento == "Pasillo":
      asiento = 'C'
   else: 
      print("Seleccione una opción correcta")
   
   Fila = randint(1,29)
   print(f"{título} {nombre_completo} su vuelo será el {num_dia}/{num_mes} desde {origen} hacia {destino} con la silla {asiento} {Fila}, por un valor de {costo}. Su vuelo quedó reservado. Gracias por volar con nosotros")

   pass 


if __name__ == "__main__":
    main()
    