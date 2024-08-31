## Diagrama de bloques 
![alt text](<Diagrama bloques-1.png>)

## Análisis 
![alt text](Variables.png)

## Pseudocódigo 

Inicio 
     
     escribir("Ingrese la altitud_inicial en km: ")
     Leer altitud_inicial

     escribir("Indique el coeficiente_arrastre: ")
     Leer coeficiente_arrastre 

     escribir("Ingrese la altitud_mínima: ")
     Leer altitud_mínima 

     Definir altitud inicial = altitud 
     Definir altitud_pérdida= 0
     Definir orbitas = 0 

    Mientras altitud > altitud_mínima 
      Calcular altitud_pérdida:
      altitud_pérdida= coeficiente_arrastre * altitud
      Calcular altitud:
      altitud= altitud_pérdida - altitud 
      Definir coeficiente_arrastre:
      coeficiente_arrastre= coeficiente-arrastre + 0.0001
      Definir orbitas:
      orbitas= orbitas + 1
      escribir("En la orbita #(orbita) la altitud es: (altitud) )
    Fin mientras 
       Si altitud_pérdida < 0.01 entonces: 
         escribir(Satélite estabilizado)
         Si altitud < altitud_mínima entonces:
         escribir("Sin conexión con el satélite)
      Fin si 
    
Fin

