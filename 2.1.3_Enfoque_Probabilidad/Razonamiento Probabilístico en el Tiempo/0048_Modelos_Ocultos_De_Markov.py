#Modelo oculto de Markov
"""
El modelo oculto de Markov (HMM, por sus siglas en inglés) es un
modelo estadístico que se utiliza para modelar secuencias de
eventos, en los que el estado subyacente no es observable
directamente, pero se puede inferir a través de observaciones.
Es decir, el modelo asume que el estado de un sistema se puede 
representar mediante una cadena de Markov, pero en lugar de 
observar directamente el estado, solo se observa una serie de 
símbolos asociados con cada estado.

En la programación, los HMM se utilizan en una variedad 
de aplicaciones, como el reconocimiento de voz, la detección de
spam, la predicción del clima, el análisis de sentimientos y el 
procesamiento del lenguaje natural. Los HMM se implementan a 
menudo utilizando bibliotecas especializadas, como hmmlearn en 
Python, que proporcionan una interfaz para entrenar y utilizar 
modelos HMM en conjuntos de datos específicos. La implementación
típica implica el uso de algoritmos de aprendizaje para estimar
los parámetros del modelo, como las probabilidades de transición
y emisión, y luego utilizar el modelo para predecir el estado 
subyacente a partir de las observaciones dadas.
"""

# Importar módulo de HMM
from hmmlearn import hmm

# Definir el modelo oculto de Markov
modelo = hmm.GaussianHMM(n_components=2)
#En esta línea se crea un objeto GaussianHMM que
#representa el modelo oculto de Markov. GaussianHMM 
#es una clase proporcionada por la librería hmmlearn
#que implementa un modelo oculto de Markov con emisiones 
#gaussianas continuas. En este caso, se está creando un modelo
#con dos estados ocultos.

# Entrenar el modelo con una secuencia de observaciones
secuencia = [[1.5], [2.0], [1.7], [2.3], [1.9]]
modelo.fit(secuencia)
#se entrena el modelo oculto de Markov utilizando la secuencia
#de observaciones secuencia. El modelo aprende los parámetros
#para generar las observaciones a partir de los estados latentes
#del modelo.

# Generar una secuencia de observaciones a partir del modelo
secuencia_generada, estados = modelo.sample(n_samples=5) 
#utiliza el modelo entrenado para generar una nueva secuencia 
#de 5 observaciones y devuelve tanto la secuencia como los 
#estados del modelo.

# Mostrar la secuencia generada y los estados del modelo
print("Secuencia generada:", secuencia_generada)
print("Estados del modelo:", estados)

#Los estados ocultos son en un HMM son las variables 
#internas del modelo que influyen en las observaciones 
#que se hacen, pero que no se pueden observar directamente.














