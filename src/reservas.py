import random 

from random import randint
def main():
   distancia = 0 
   costo = 0
   título = input("Ingrese su título (Sr o Sra) ")
   nombre_completo = input("Ingrese su nombre completo: ")
   if título == ("Sr"):
     print(f"{título} {nombre_completo} Bienvenido a Sky Airlines")
   elif título == ("Sra"):
     print(f"{título}{nombre_completo} Bienvenido a Sky Airlines")
   ciudades = ['Medellín', 'Bogotá', 'Cartagena']
   origen = (input("Ingrese la ciudad de origen (Medellín, Bogotá, Cartagena)"))
   if origen not in ciudades: 
      print("Ciudad de origen incorrecta, seleccione nuevamente")
   destino = (input("Ingrese la ciudad de destino (Medellín, Bogotá, Cartagena)"))
   if destino not in ciudades: 
      print("Ciudad de destino incorrecta, seleccione nuevamente")
   elif origen == ciudades[0] and destino == ciudades[1]:
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
   
   num_sem = int(input("Ingrese el día de la semana en el que viajará: \nLunes(1) \nMartes(2) \nMiércoles(3) \nJueves(4) \nViernes(5) \nSábado(6) \nDomingo(7): "))
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
   
   Asiento = input("Ingrese el lugar de su preferencia: \nA: Ventana \nB: Sin preferencia \nC: Pasillo  ")
   Fila = randint(1,29)
   print(f"{título} {nombre_completo} el vuelo será el {num_dia}/{num_mes} con la silla {Asiento} {Fila}, con un valor de {costo}. Su vuelo quedó reservado. Gracias por volar con nosotros")

   pass

    


   
      




































if __name__ == "__main__":
    main()