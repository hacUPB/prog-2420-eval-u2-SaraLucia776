sum

Lista = [4,5,7,34,54,65,76,3,4,54,34,23,22,11]
acum = 0
cont = 0 

num_elem = len(Lista)

while cont < num_elem: 
    acum += Lista[cont]
    cont += 1

sumatoria = sum(Lista)
print(f"Si el código es correcto, {acum} = {sumatoria}")

acum = 0 
for elemento in Lista:
    acum += elemento 

print(f"Usando el bucle for la suma es {acum}")


max 

Lista = [2,30,8]
mayor = Lista[0]

for elemento in Lista:
 if elemento > mayor:
    mayor = elemento 
print(elemento)
