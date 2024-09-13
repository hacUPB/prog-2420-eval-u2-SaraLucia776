import time

def main():
    alt_inicial = float(input("Ingrese la altitud inicial del satélite (en Km): "))
    coe_arrastre = float(input("Ingrese el coeficiente de arrastre inicial: "))
    alt_min_seg = float(input("Ingrese la altitud mínima de seguridad (en Km): "))
    orbitas = 0

    # Cuando la altitud dada es menor a la altitud mínima de seguridad
    if alt_inicial < alt_min_seg:
        print("El satélite se encuentra por debajo de la altitud mínima de seguridad")
    
    # Cáculo de las orbitas y altitud en cada una
    while alt_inicial > alt_min_seg:
        altitud_perdida = coe_arrastre * alt_inicial
        if altitud_perdida < 0.5:
            print("Satélite se ha estabilizado")
        else:
            alt_inicial = alt_inicial - altitud_perdida
            coe_arrastre += 0.0001
            orbitas += 1
            print(f"Órbita: {orbitas}, Altitud actual:  {alt_inicial}, Coeficiente de arrastre:  {coe_arrastre}")
    print(f"Número total de órbitas:  {orbitas} ")   
    

if __name__ == "__main__":
    main()
