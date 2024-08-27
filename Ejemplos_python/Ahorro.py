suma = 0 
n = 1 

while n <= 365:
    valor = 3 ** n 
    suma += valor
    n += 1 

pesos = suma / 100
print(f"El total ahorrado es ${pesos}")