suma = 0 
número = int(input("Ingrese el número de estudiantes: "))
cont = 1

while cont <= número: 
    edad = int(input("Ingrese la edad: "))
    suma = suma + edad 
    cont = cont + 1 

promedio = suma / número 
print(f"Promedio de edades = {promedio}")



