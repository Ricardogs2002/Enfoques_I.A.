# Importamos la biblioteca numpy
import numpy as np

# Definimos los estados posibles del clima. En este caso, consideramos tres estados posibles: soleado (S), nublado (N) y lluvioso (L).
estados = ["S", "N", "L"]

# Definimos la matriz de transición que contiene la probabilidad de pasar de un estado a otro.
# En este caso, asumimos que las probabilidades son las siguientes:
# - La probabilidad de que el clima sea soleado después de un día soleado es del 70%
# - La probabilidad de que el clima sea nublado después de un día soleado es del 20%
# - La probabilidad de que el clima sea lluvioso después de un día soleado es del 10%
transiciones = np.array([
    [0.7, 0.2, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

# Definimos la distribución de probabilidad inicial, que representa la probabilidad de cada estado al comienzo del proceso.
inicial = np.array([0.6, 0.3, 0.1])

# Ahora, podemos usar el modelo de Markov para predecir el clima en los próximos días. 
# Para hacer esto, multiplicamos la distribución de probabilidad inicial por la matriz de transición una vez para obtener 
# la distribución de probabilidad del primer día, y luego continuamos multiplicando la distribución de probabilidad del día 
# anterior por la matriz de transición para obtener la distribución de probabilidad del día siguiente.

# Especificamos cuántos días queremos predecir el clima
dias = 7

# Creamos una matriz vacía para almacenar las predicciones de probabilidad del clima para cada día
prediccion = np.zeros((dias, 3))
# Establecemos la distribución de probabilidad inicial como la primera fila de la matriz de predicción
prediccion[0] = inicial

# Iteramos sobre los días restantes y calculamos la distribución de probabilidad del clima para cada día
for i in range(1, dias):
    prediccion[i] = np.dot(prediccion[i-1], transiciones)

# Imprimimos la matriz de predicción que muestra la distribución de probabilidad del clima para cada día
print(prediccion)
