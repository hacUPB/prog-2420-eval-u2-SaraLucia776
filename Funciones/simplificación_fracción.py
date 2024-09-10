# Simplificar la fracción 
# Calcular divisores del numerador y del denominador
# Seleccionar el divisor común mayor

from módulo_fracción import *

n1 = int(input("Ingrese el numerador: "))
n2 = int(input("Ingrese el denominador: "))

lista_num = calcula_divisores(n1)
lista_den = calcula_divisores(n2)
print(f"Divisores del numerador {lista_num}")
print(f"Divisores del denorminador {lista_den}")

mcd = máx_com_div(lista_num, lista_den)

simplificación = simplifica_fracción(n1,n2,mcd)
