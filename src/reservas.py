import random 
import datetime
from random import randint

# Profe, el código está relativamente bien, funciona y los datos que entrega son correctos. Pero tiene un pequeño inconveniente con los espacios, 
# si de pronto escojo la ciudad de origen y escribo Medellín y dejo un espacio al final, al darle enter sale como si la ciudad fuese incorrecta. 

def main():
   distancia = 0 
   costo = 0
   ciudades = ['Medellín', 'Bogotá', 'Cartagena']
   
   # Datos del usuario 
   título = input("Ingrese su título (Sr o Sra) ").capitalize()
   nombre_completo = input("Ingrese su nombre completo: ")
   
   if título == ("Sr"):
     print(f" {título} {nombre_completo} Bienvenido a Sky Airlines")
   elif título == ("Sra"):
     print(f"{título} {nombre_completo} Bienvenida a Sky Airlines")

   # Ciudad de origen y destino
   origen = str(input("Ingrese la ciudad de origen (Medellín, Bogotá, Cartagena)"))
   while True:
      if origen not in ciudades: 
         print("Ciudad de origen incorrecta, seleccione nuevamente")
         origen = str(input("Ingrese la ciudad de origen (Medellín, Bogotá, Cartagena)"))
      else:
         break
   
   destino = str(input("Ingrese la ciudad de destino (Medellín, Bogotá, Cartagena ) "))
   while True:
      if destino not in ciudades: 
         print("Ciudad de destino incorrecta, seleccione nuevamente")
         destino = str(input("Ingrese la ciudad de destino (Medellín, Bogotá, Cartagena ) "))
      else:
         break 
   
   # Fecha del viaje, costo y distancia
   num_dia = int(input("Ingrese el día del mes en el que viajará "))
   num_mes = int(input("Ingrese el número del mes en el que viajará "))
   
   num_año = int(input("Ingrese el año en el que desea viajar"))
   while True:
      if num_año < 2024:
         print("Ingrese un año válido")
         num_año = int(input("Ingrese el año en el que desea viajar"))
      else:
         break    

   fecha = datetime.datetime(num_año,num_mes,num_dia)
   dias_semana = [1,2,3,4]
   dias_fin_semana = [5,6,7]
   
   if origen == ciudades[0] and destino == ciudades[1] or origen == ciudades[1] and destino == ciudades[0]: 
      distancia = 241
      if fecha.isoweekday() in dias_semana:
         costo = 79900
      else: 
         costo = 119900
   elif origen == ciudades[0] and destino == ciudades[2] or origen == ciudades[2] and destino == ciudades[0]:
      distancia = 461 
      if fecha.isoweekday() in dias_semana:
         costo = 156900
      else: 
         costo = 213000
   elif origen == ciudades[1] and destino == ciudades[2] or origen == ciudades[2] and destino == ciudades[1]:
      distancia = 657
      if fecha.isoweekday() in dias_semana: 
         costo = 156900
      else: 
         costo = 213000
   else: 
      print("Viaje no disponible")
   
   # Selección de la silla 
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
   print(f"{título} {nombre_completo} su vuelo será el {num_dia}/{num_mes}/{num_año} desde {origen} hacia {destino} con la silla {asiento}{Fila}, por un valor de {costo}. Su vuelo quedó reservado. Gracias por volar con nosotros")

   pass 

if __name__ == "__main__":
   main()
    