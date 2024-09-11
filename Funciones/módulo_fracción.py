def calcula_divisores(numero:int):
    divisores = []
    for divisor in range(1,numero +1 ):
       if numero % divisor == 0:
           divisores. append(divisor)
    return divisores

def máx_com_div(lista1:list, lista2:list):
    elem_l1 = len(lista1)  #Calcula el número de elementos que tiene la lista
    for i in range(elem_l1 -1, -1, -1): #Genera un bucle desde le número máximo hata llegar a cero 
       if lista2.count(lista1[i] ) == 1: #Compara los elementos de i de la lista uno con los de la lista dos
         return lista1[i]
    return -1 

def simplifica_fracción(num1:int, num2:int, mcd:int):   # Imprimir la fracción original y simplificada 
   numerador = num1 / mcd
   denominador = num2 / mcd 
   
   print(f"{num1} / {num2} = {numerador} / {denominador}")