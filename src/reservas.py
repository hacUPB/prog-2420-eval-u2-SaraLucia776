import random 
import datetime
from random import randint

# Profe, el código está relativamente bien, funciona y los datos que entrega son correctos. Pero tiene un pequeño inconveniente con los espacios, 
# si de pronto escojo la ciudad de origen y escribo Medellín y dejo un espacio al final, al darle enter sale como si la ciudad fuese incorrecta. 

def main():
   distancia = 0 
   costo = 0
   ciudades = ['Medellín', 'medellin','Medellin', 'medellín', 'Bogotá', 'bogota', 'Bogota', 'bogotá', 'Cartagena', 'cartagena']
   
   # Datos del usuario
   nombre_completo = input("Ingrese su nombre completo: ")
   while True:
      título = input("Ingrese su título (Sr o Sra) ").capitalize()
      if título == ("Sr"):
         print(f"{título} {nombre_completo} Bienvenido a Sky Airlines")
         break
      elif título == ("Sra"):
         print(f"{título} {nombre_completo} Bienvenida a Sky Airlines")
         break
      else:
         print("Escriba un titulo correcto.")
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

   # Ciudad de origen y destino
   while True:
      origen = str(input("Ingrese la ciudad de origen (Medellín, Bogotá, Cartagena)"))
      destino = str(input("Ingrese la ciudad de destino (Medellín, Bogotá, Cartagena ) "))
      if origen not in ciudades: 
         print("Ciudad de origen incorrecta, seleccione nuevamente")
      elif destino not in ciudades: 
         print("Ciudad de destino incorrecta, seleccione nuevamente")
      elif destino == origen:
         print("Viaje no disponible")
      else:
         break 
   

   fecha = datetime.datetime(num_año,num_mes,num_dia)
   dias_semana = [0,1,2,3]
   dias_fin_semana = [4,5,6]
   while True:   
      if origen == ciudades[0:4] and destino == ciudades[4:8] or origen == ciudades[4:8] and destino == ciudades[0:4]: 
         if fecha.isoweekday() in dias_semana:
            costo = 79900         
         else: 
            costo = 119900
         break
      elif origen == ciudades[0:4] and destino == ciudades[8:9] or origen == ciudades[8:9] and destino == ciudades[0:4]:
         if fecha.isoweekday() in dias_semana:
            costo = 156900            
         else: 
            costo = 213000      
         break      
      elif origen == ciudades[4:8] and destino == ciudades[8:9] or origen == ciudades[8:9] and destino == ciudades[4:8]:
         if fecha.isoweekday() in dias_semana: 
            costo = 156900            
         else: 
            costo = 213000
         break
   # Selección de la silla 
   while True:
      asiento = (input("Ingrese el asiento de su preferencia (Ventana, Sin preferencia, Pasillo)"))
      if asiento == "Ventana" or asiento == 'ventana':
         asiento = 'A'
         break
      elif asiento == "Sin preferencia" or asiento == 'sin preferencia':
         asiento = 'B' 
         break
      elif asiento == "Pasillo" or asiento == 'pasillo':
         asiento = 'C'
         break
      else: 
         print("Seleccione una opción correcta")
   Fila = randint(1,29)
   print(f"{título} {nombre_completo} su vuelo será el {num_dia}/{num_mes}/{num_año} desde {origen} hacia {destino} con la silla {asiento}{Fila}, por un valor de {costo}. Su vuelo quedó reservado. Gracias por volar con nosotros")

   pass 

if __name__ == "__main__":
   main()
    