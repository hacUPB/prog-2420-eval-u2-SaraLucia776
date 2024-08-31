## Diagrama de bloques 

![alt text](<Diagrama de bloques Reserva.png>)

## Análisis 

![alt text](<Tabla variables.png>)
Todas la variables de entrada deben ser dadas por el usuario, para lograr el funcionamiento del pseudocódigo

## Pseudocódigo 

    Inicio 
    escribir("Sr ó Sra")
    Leer título        
    
    escribir("Ingrese su nombre_completo")
    Leer nombre completo

    escribir("Bienvenido a FastFast Airlines")                                 

    escribir("Escoja origen: Medellín, Bogotá, Cartagena")
    Leer origen 

    escribir("Escoja destino: Medellín, Bogotá, Cartagena")
    Leer destino 

    escribir("Seleccione día_semana entre 1 y 7)
    Leer día

    escribir("Seleccione día_mes que desea viajar entre 1 y 30)
    Leer día del mes 

    Si Origen= Medellín y Destino= Bogotá o Origen= Bogotá y Destino= Medellín:
            Distancia= 240 km 
                Si día <= 4: 
                Costo = 79,900
                    Si no 
                    Costo = 119,900
    Fin si 
    
    Si Origen= Medellín y Destino= Cartagena o Origen= Cartagena y Destino= Medellín:
            Distancia = 461 km 
                Si día <= 4:
                Costo = 156,900
                    Si no 
                    Costo = 213,000
    Fin si 
    
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
    
    escribir("(Título)(Nombre_completo)su vuelo tendrá un valor de $(Costo)el (Día_semana)(Día_mes) y su silla será (Asiento)(Fila))
    escribir("Gracias por volar con nosotros")

    Fin


