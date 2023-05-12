#Mapas Auto-organizados de Kohonen
"""
Los Mapas Auto-Organizados de Kohonen (también conocidos como
SOM, por sus siglas en inglés) son una técnica de aprendizaje no
supervisado en el campo del procesamiento de señales y la
inteligencia artificial.

Los SOM se utilizan para explorar relaciones en conjuntos de datos
complejos y de alta dimensión. El objetivo de la técnica es 
reducir la dimensión de los datos, preservando las 
características esenciales de los mismos y representándolos en 
un espacio bidimensional o tridimensional para su visualización.

Los SOM se basan en una red neuronal artificial compuesta por 
nodos que se organizan en una matriz bidimensional o 
tridimensional. Cada nodo se asocia a un vector de características
y el conjunto de nodos se agrupa en torno a regiones con 
características similares.
"""

# Importar módulo de SOM
from minisom import MiniSom #Se importa la librería MiniSom.
import numpy as np #Se importa la librería NumPy.

# Definir la matriz de datos
datos = np.array([[1.2, 2.3], [2.1, 1.7], [1.9, 1.4], [1.5, 2.0]])
#Se define la matriz de datos como un arreglo NumPy de 4 filas y 2 columnas, con valores flotantes.

# Definir el tamaño del mapa auto-organizado
tamanio_mapa = (2, 2)

# Crear el mapa auto-organizado y entrenarlo
modelo = MiniSom(tamanio_mapa[0], tamanio_mapa[1], datos.shape[1])
#Se define el tamaño del mapa auto-organizado como una tupla de 2x2.
#Se crea una instancia de la clase MiniSom, con el tamaño del mapa y el número de características de los datos.

modelo.train_random(datos, 100)

# Mostrar el mapa auto-organizado y las neuronas ganadoras para cada dato
#Se entrena el modelo con los datos utilizando el método "train_random", que es un método de entrenamiento que utiliza el algoritmo de Kohonen.
#Se muestra el mapa auto-organizado y las neuronas ganadoras para cada dato en un bucle "for". El método "winner" devuelve la neurona ganadora para
#cada dato, y el método "get_weights" devuelve los pesos de las neuronas del mapa.

for i, x in enumerate(datos):
    ganador = modelo.winner(x)
    print("Dato:", x, "- Neurona ganadora:", ganador)
    print("Mapa auto-organizado:")
    print(modelo.get_weights())
#Se entrena el modelo con los datos utilizando el método "train_random", que es un método de entrenamiento que utiliza el algoritmo de Kohonen.
#Se muestra el mapa auto-organizado y las neuronas ganadoras para cada dato en un bucle "for". El método "winner" devuelve la neurona ganadora para cada dato,
#y el método "get_weights" devuelve los pesos de las neuronas del mapa.
#Los mapas auto-organizados de Kohonen son una técnica de aprendizaje no supervisado utilizada para la visualización y agrupamiento de datos. Consiste en una 
#red neuronal artificial que organiza los datos en una estructura de mapa
#bidimensional, donde cada neurona en el mapa corresponde a un vector de pesos que se ajusta durante el entrenamiento. Los mapas auto-organizados son útiles 
#para descubrir patrones en los datos y para visualizar estructuras complejas 
#en conjuntos de datos de alta dimensión.
