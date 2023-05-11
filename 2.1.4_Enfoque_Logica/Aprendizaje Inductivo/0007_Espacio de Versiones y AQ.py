"""
El Espacio de Versiones se refiere a un conjunto de hipótesis que son consistentes con los datos de entrenamiento 
disponibles. En otras palabras, es el espacio de todas las posibles soluciones que pueden ser obtenidas de un 
conjunto de datos de entrenamiento. El objetivo de la técnica de Espacio de Versiones es reducir este conjunto 
de soluciones a una hipótesis única que pueda ser utilizada para predecir valores desconocidos.

Por otro lado, la Consulta Adaptativa es un proceso de selección de datos de entrenamiento adicionales que se 
utiliza para refinar aún más el Espacio de Versiones. En la Consulta Adaptativa, se seleccionan datos de 
entrenamiento de forma inteligente con el objetivo de eliminar hipótesis inconsistentes y reducir el Espacio 
de Versiones.

Ambos conceptos son de gran importancia en la resolución de problemas de clasificación, y su uso conjunto
 puede mejorar significativamente el rendimiento de un modelo de clasificación. La técnica de Espacio de Versiones 
 permite la construcción de un modelo consistente con los datos de entrenamiento disponibles, mientras que la 
 Consulta Adaptativa permite la selección inteligente de datos de entrenamiento adicionales para refinar aún más 
 el modelo.

En resumen, el Espacio de Versiones y la Consulta Adaptativa son herramientas esenciales en la construcción de 
modelos de clasificación efectivos. Con estas técnicas, podemos obtener modelos precisos y eficientes que pueden 
ser aplicados en una amplia gama de problemas en el campo de la Inteligencia Artificial.
"""
import numpy as np
import random

# Función para generar el espacio de versiones
def version_space(train_data):
    hypotheses = []
    # Recorre todos los ejemplos de entrenamiento
    for instance in train_data:
        # Separa los atributos y la etiqueta de la instancia
        x, y = instance[:-1], instance[-1]
        # Si la etiqueta es 1, agrega una hipótesis al espacio de versiones que evalúa si todos los atributos son iguales a la instancia
        if y == 1:
            hypotheses.append(lambda z: all([z[i] == x[i] for i in range(len(x))]))
        # Si la etiqueta es -1, agrega una hipótesis al espacio de versiones que evalúa si al menos un atributo es diferente a la instancia
        else:
            hypotheses.append(lambda z: not all([z[i] == x[i] for i in range(len(x))]))
    return hypotheses

# Función para realizar una consulta adaptativa
def adaptive_querying(train_data, budget):
    # Genera el espacio de versiones
    hypotheses = version_space(train_data)
    # Selecciona aleatoriamente un conjunto de ejemplos de entrenamiento para hacer consultas
    query_indices = random.sample(range(len(train_data)), budget)
    query_set = train_data[query_indices]
    # Actualiza el espacio de versiones eliminando hipótesis inconsistentes con las respuestas obtenidas de las consultas
    for instance in query_set:
        x, y = instance[:-1], instance[-1]
        hypotheses = [h for h in hypotheses if h(x) == (y == 1)]
    return hypotheses

# Función para predecir la etiqueta de una instancia utilizando el espacio de versiones
def predict(hypotheses, instance):
    # Recorre todas las hipótesis en el espacio de versiones
    for h in hypotheses:
        # Si una hipótesis evalúa a Verdadero para una instancia, retorna la etiqueta positiva
        if h(instance[:-1]):
            return 1
    # Si ninguna hipótesis evaluó a Verdadero, retorna la etiqueta negativa
    return -1

# Conjunto de ejemplos de entrenamiento
train_data = np.array([[1, 1, 0, 1],
                       [0, 0, 1, -1],
                       [1, 0, 1, 1],
                       [0, 1, 0, -1],
                       [0, 1, 1, -1],
                       [1, 0, 0, -1],
                       [1, 1, 1, 1],
                       [0, 0, 0, -1]])

# Conjunto de ejemplos de prueba
test_data = np.array([[1, 0, 0, -1],
                      [1, 1, 0, 1],
                      [0, 1, 1, -1],
                      [1, 0, 1, 1]])

# Genera el espacio de versiones adaptativo utilizando 3 ejemplos de entrenamiento
hypotheses = adaptive_querying(train_data, 3)

# Realiza la predicción para cada ejemplo de prueba y muestra el resultado
for instance in test_data:
    print(instance[:-1], predict(hypotheses, instance))
