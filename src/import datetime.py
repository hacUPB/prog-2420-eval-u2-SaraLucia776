import datetime
num_dia = int(input("Ingrese el día del mes en el que viajará "))
num_mes = int(input("Ingrese el número del mes en el que viajará "))
num_año = int(input("Igrese el año que desea viajar"))

fecha = datetime.datetime(num_año,num_mes,num_dia)
print(fecha.isoweekday())
dias_de_semana = [1,2,3,4]
if fecha.isoweekday() in dias_de_semana:
    price = 80000
else:
    price = 170000

print(f"Precio de boleto es {price}") 

ciudades = ["Bogotá","Cartagena","Medellín"]
origen = str(input("Ciudad de origen:  "))
destino = str(input("Ciudad de destino"))

if (origen == "Bogotá" and destino == "Medellín") or (origen == "Medellín" and destino=="Bogotá"):
    distancia = 500
    price = 50000
    if fecha.isoweekday() in dias_de_semana:
        price = 80000
    else:
        price = 170000
else:
    print("Viaje no disponible")

    print(fecha.isoweekday())