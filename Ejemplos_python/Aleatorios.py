import random

from random import randit, uniform

#Creo una lista vacía 
aleatorios = []

#Generar un número aleatorio 
num_aleatorio = randit(10,150)

#Ingresar el número a la lista 
aleatorios.append(num_aleatorio)
print(aleatorios)

#Genero 100 números aleatorios y los agrego a la lista 
for i in range(100):
     #Generar un número aleatorio
     num_aleatorio = randit(10,150)
     #Ingresar el número a la lista 
     aleatorios.append(num_aleatorio)
print(aleatorios)
