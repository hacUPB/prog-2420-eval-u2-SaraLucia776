## Diagrama de bloques 

![alt text](<Diagrama de bloques Reserva.png>)

## Análisis 

![alt text](<Tabla variables.png>)


## Pseudocódigo 

Inicio 
 escribir("Sr ó Sra")
 Leer título        
 
 escribir("Ingrese su nombre completo")
 Leer nombre completo

 escribir("Bienvenido a FastFast Airlines")                                 

 escribir("Escoja lugar de origen: Medellín, Bogotá, Cartagena")
 Leer lugar de origen 

 escribir("Escoja lugar de destino: Medellín, Bogotá, Cartagena")
 Leer lugar de destino 

 escribir("Seleccione día de la semana entre 1 y 7)
 Leer día

 escribir("Seleccione día del mes que desea viajar entre 1 y 30)
 Leer día del mes 

  Si Origen= Medellín y Destino= Bogotá o Origen= Bogotá y Destino= Medellín:
        Distancia= 240 km 
            Si día <= 4: 
            Costo = 79,900
                Si no 
                Costo = 119,900
  
  Si Origen= Medellín y Destino= Cartagena o Origen= Cartagena y Destino= Medellín:
        Distancia = 461 km 
            Si día <= 4:
            Costo = 156,900
                Si no 
                Costo = 213,000

  Si Origen= Bogotá y Destino= Cartagena o Oringen= Cartagena y Destino= Bogotá:
         Distancia= 657 km
            Si día <= 4: 
            Costo = 156,900
                Si no 
                Costo = 213,000
 Fin Si 
    
 escribir("Seleccione su asiento (A:Pasillo, C:Ventana, B:Sin preferencia):" )
 Leer selección de asiento

 Definir Fila = número aleatorio (1,29) 
 
 escribir("(Título)(Nombre y apellido)su vuelo tendrá un valor de $(Costo)el (Día_semana)(Día_mes) y su silla será (Asiento)(Fila))
 escribir("Gracias por volar con nosotros")

Fin


