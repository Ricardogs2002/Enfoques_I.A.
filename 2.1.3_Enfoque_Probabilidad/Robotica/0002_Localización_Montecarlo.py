"""El método Monte Carlo se basa en la generación de muestras aleatorias para
aproximar una solución numérica. Para ello, se utilizan técnicas de simulación
que permiten generar muestras aleatorias de una distribución de probabilidad
conocida o desconocida, y a partir de estas muestras se realizan cálculos
estadísticos para obtener estimaciones de parámetros y soluciones de problemas."""

import random

# Definimos el número de puntos a generar
num_puntos = 1000000
# Contador de puntos dentro del círculo
dentro_circulo = 0

# Generamos los puntos aleatorios y los contamos
for i in range(num_puntos):
    # Generamos un punto aleatorio dentro del cuadrado
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # Calculamos la distancia al origen
    distancia = (x**2 + y**2)**0.5
    # Si la distancia es menor o igual a 1, el punto está dentro del círculo
    if distancia <= 1:
        dentro_circulo += 1

# Estimamos el valor de pi
pi_estimado = 4 * dentro_circulo / num_puntos

# Imprimimos el resultado
print(f"Valor estimado de pi: {pi_estimado}")
