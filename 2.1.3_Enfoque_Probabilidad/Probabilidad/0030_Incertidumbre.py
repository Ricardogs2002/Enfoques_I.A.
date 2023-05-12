#Incertidumbre
"""
La incertidumbre se refiere a la falta de conocimiento o 
información precisa sobre un evento o situación. En programación,
la incertidumbre puede manifestarse de varias maneras, como
la variabilidad en los datos de entrada, la posibilidad de 
fallos en el hardware o software, la falta de conocimiento 
sobre la estructura o comportamiento de un sistema, entre 
otros.

Una forma de abordar la incertidumbre en programación es 
mediante el uso de técnicas de inferencia y razonamiento 
probabilístico. Por ejemplo, se pueden utilizar algoritmos 
de aprendizaje automático para analizar y clasificar datos que
tienen una cierta variabilidad o imprecisión, o se pueden 
implementar sistemas de lógica difusa para modelar situaciones
en las que no hay una frontera clara entre las categorías.
"""
#Importar módulo de incertidumbre
import numpy as np

# Definir un arreglo de probabilidades
probabilidades = np.array([0.2, 0.5, 0.3])

# Calcular la entropía de Shannon
#se define la función entropia_shannon, que calcula 
#la entropía de Shannon de un arreglo de probabilidades.
#Esta función toma un arreglo de probabilidades como entrada 
#y devuelve un valor numérico que representa la entropía.
def entropia_shannon(p):
    entropia = 0
    for i in range(len(p)):
        if p[i] > 0:
            entropia -= p[i] * np.log2(p[i])
    return entropia
#La variable entropia se inicializa en cero. Luego, 
#se realiza un bucle for que itera sobre cada elemento 
#del arreglo de probabilidades. Si el elemento es mayor 
#que cero, se calcula la contribución de ese elemento a la 
#entropía utilizando la fórmula de Shannon, que es -p * log2(p).
#El resultado se resta de la variable entropia.

# Calcular la entropía de Shannon del arreglo de probabilidades
entropia = entropia_shannon(probabilidades)
print("La entropía de Shannon es:", entropia)

#La entropía de Shannon es una medida de la incertidumbre 
#en un conjunto de datos o eventos.