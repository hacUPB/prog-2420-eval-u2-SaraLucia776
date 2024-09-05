# Función que recibe: 1. Número de elementos. 2. Rango de valores y retorna una lista 
# La función recibe una lista de números flotantes y retorna su promedio 
# Calcula cuantos elementos están por encima del promedio de una lista y retorna ese valor 

from random import uniform 

# Función 1 
def crea_lista(cantidad:int, lim_inf:float, lim_sup:float): # Parámetros de la función
    # 1. Crear la lista vacía 
    lista = []
    # 2. Utilizar un bucle para llenar la lista
    for i in range(cantidad):
        # 3. Se genera el número aleatorio
        num_aleat = uniform(lim_inf, lim_sup)
        # 4. Se agrega el número a la lista 
        lista. append(num_aleat)
    return lista


# Función 2
def calcula_promedio(datos:list):  # Datos es una lista de números de punto flotante
    prom = sum(datos)/ len(datos)
    return prom

# Función 3 
def sobre_promedio(datos:list, promedio:float):
    cont = 0 
    mayores = [] # Lista para guardar los valores mayores al promedio
    for i in datos: 
       if i < promedio: 
           cont += 1 
           mayores. append(i)
    return cont, mayores

           
           
# Programa principal 
aleatorios = crea_lista(100, 0.0, 10.0)
print(aleatorios)
promedio = calcula_promedio(aleatorios)
print(f"El promedio es {promedio}")
cant, lista_mayores = sobre_promedio(aleatorios, promedio)
print(f"Hay {cant} valores mayores al promedio y son: {lista_mayores}")

