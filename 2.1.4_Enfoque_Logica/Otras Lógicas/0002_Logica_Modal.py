
import random
import time

# Establecemos el umbral de cambio de estado, porcentaje de tendencia
umbral = 0.8      #Reducir para aumentar los eventos

# Estado inicial
estado = "No se detecta movimiento"

# Ciclo principal
while True:
    # Generamos un número aleatorio
    aleatorio = random.random()

    # Verificamos si cambiamos de estado
    if aleatorio > umbral:
        estado = "Movimiento detectado!!!             Encendiendo luces                  Activando Alarma    "
    else:
        estado = "No se detecta movimiento"

    # Imprimimos el estado actual
    print(estado)

    # Esperamos un segundo antes de continuar
    time.sleep(1)

