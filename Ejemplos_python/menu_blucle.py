from os import system

while True: #Bucle infinito 
    print("1. Calcular primo\n2. Calcular par\n3. Salir")
    opción = int(input("Ingrese la opción: "))

    if opción == 1:
        system("cls")
        print("Calcular si el número es primo")
        número = int(input("Ingrese el número a probar: "))
        control = 1 
        cont = 0
        
        while control <= número: 
           if (número % control) == 0:
              cont += 1
           control += 1 
       
        if cont > 2:
           print(f"{número} no es primo")
        else: 
          print(f"{número} es primo")
    
    elif opción == 2:
       número = int(input("Ingrese el número a probar: "))
       
       if número % 2 == 0:
          print(f"{número} es par")
       else:
          print(f"{número} es impar")
    
    elif opción == 3:
       break 
    else: 
       print("Opción no válida...")
