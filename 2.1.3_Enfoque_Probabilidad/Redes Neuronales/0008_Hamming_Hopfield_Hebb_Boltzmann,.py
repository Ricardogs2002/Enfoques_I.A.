

import numpy as np
import matplotlib.pyplot as plt


######################     código de Hamming

print("\n\n codigo de hamming \n\n")
"""
El código de Hamming es una técnica que se utiliza en la transmisión de datos digitales para detectar 
y corregir errores, lo que es fundamental para el correcto funcionamiento de los sistemas de inteligencia artificial.

Por ejemplo, en los sistemas de reconocimiento de voz, los errores en la transmisión de los datos de 
audio pueden dar lugar a una interpretación errónea de las palabras habladas, lo que puede afectar significativamente 
la precisión del reconocimiento de voz. El uso del código de Hamming en la transmisión de los datos de audio ayuda 
a detectar y corregir estos errores, lo que mejora la precisión del reconocimiento de voz.

Además, el código de Hamming también se utiliza en el diseño de las redes neuronales artificiales, que son un 
componente clave de muchos sistemas de inteligencia artificial. Los errores en los datos de entrada o salida de 
la red pueden afectar significativamente su funcionamiento y su capacidad para aprender patrones y relaciones en 
los datos. El uso del código de Hamming para detectar y corregir estos errores ayuda a mejorar la precisión y 
la eficacia de la red.

En resumen, el código de Hamming es una técnica importante en la transmisión de datos digitales que también 
se aplica en el diseño y la operación de sistemas de inteligencia artificial, lo que contribuye a mejorar su 
precisión y su capacidad para procesar y aprender de los datos.
"""
def hamming_distance(s1, s2):
    """
    Calcula la distancia de Hamming entre dos cadenas de igual longitud.
    """
    if len(s1) != len(s2):
        raise ValueError("Las cadenas deben tener la misma longitud.")
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

# Ejemplo de uso
cadena1 = '01010101'
cadena2 = '01100110'
distancia = hamming_distance(cadena1, cadena2)
print(f"La distancia de Hamming entre {cadena1} y {cadena2} es {distancia}")

"""
 La distancia de Hamming entre las cadenas 01010101 y 01100110 es 4, 
 porque hay cuatro posiciones en las que los símbolos correspondientes de ambas 
 cadenas son diferentes: las posiciones 2, 3, 6 y 7.
"""


###############################          red de Hopfield


print("\n\n red de hopfield\n\n")

"""
Una red de Hopfield es un tipo de red neuronal recurrente que se utiliza para el reconocimiento de patrones 
y la corrección de errores. Esta red está diseñada para almacenar un conjunto de patrones y luego recuperarlos 
a partir de patrones incompletos o distorsionados.

La red de Hopfield se compone de nodos o neuronas interconectados por sinapsis de peso variable. 
Los nodos pueden estar en uno de dos estados: "encendido" o "apagado", que se representan típicamente 
como 1 y -1, respectivamente. Los pesos de las sinapsis se ajustan de tal manera que, cuando se presenta un 
patrón a la red, las neuronas correspondientes se activan y envían señales a las neuronas vecinas. A medida que 
la señal se propaga a través de la red, se produce una respuesta coherente que representa el patrón de entrada.

Durante la fase de entrenamiento, se presenta una serie de patrones a la red y se ajustan los pesos de las sinapsis 
para que se almacenen los patrones. En la fase de recuperación, se presenta un patrón incompleto o distorsionado 
a la red, y la red trata de encontrar el patrón más cercano que corresponde a ese patrón incompleto o distorsionado.

La red de Hopfield se utiliza en diversas aplicaciones, como la corrección de errores en sistemas 
de transmisión de datos y la restauración de imágenes distorsionadas.
"""


# Función de activación
def activation(x):
    return np.sign(x)

# Patrones de imagen
patterns = np.array([
    [-1, 1, -1, 1,
     1, -1, -1, 1,
     1, -1, -1, 1,
     1, -1, -1, 1],
    
    [1, 1, 1, 1,
     -1, -1, -1, -1,
     -1, -1, -1, -1,
     1, 1, 1, 1],
    
    [-1, 1, 1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, 1, 1, -1],
    
    [1, 1, 1, 1,
     1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1]
])

# Imágenes distorsionadas
distorted_patterns = np.array([
    [-1, 1, -1, 1,
     1, 1, -1, 1,
     1, -1, -1, 1,
     1, -1, -1, 1],
    
    [1, 1, 1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, -1, -1, 1],
    
    [-1, 1, 1, -1,
     1, -1, -1, -1,
     -1, -1, -1, -1,
     -1, 1, -1, -1],
    
    [1, -1, -1, -1,
     1, -1, -1, 1,
     -1, -1, -1, -1,
     -1, -1, -1, 1]
])

# Inicializar matriz de pesos
W = np.zeros((patterns.shape[1], patterns.shape[1]))

# Entrenamiento
for pattern in patterns:
    pattern = pattern.reshape(-1, 1) # Convertir el patrón en un vector columna
    W += np.dot(pattern, pattern.T) # Actualizar la matriz de pesos

# Diagonal con ceros
np.fill_diagonal(W, 0) # La diagonal de la matriz de pesos se pone en 0

# Corrección de patrones distorsionados
for distorted_pattern in distorted_patterns:
    distorted_pattern = distorted_pattern.reshape(-1, 1) # Convertir la imagen distorsionada en un vector columna
    output = distorted_pattern.copy() # Inicializar la salida con la imagen distorsionada
    prev_output = np.zeros(output.shape) # Inicializar la salida previa
    counter = 0 # Contador de iteraciones
    while not np.array_equal(output, prev_output) and counter < 100:
        prev_output = output.copy() # Actualizar la salida previa
        for i in range(output.shape[0]):
            output[i] = activation(np.dot(W[i, :], output)) # Aplicar la regla de actualización a cada neurona
        counter += 1 # Incrementar el contador de iteraciones
    
    # Mostrar imágenes
    plt.figure()
    plt.subplot(121)
    plt.imshow(distorted_pattern.reshape(4, 4), cmap='gray')
    plt.title('Imagen Distorcionada')
    plt.subplot(122)
    plt.title('Imagen corregida')
    plt.imshow(output.reshape(4, 4), cmap='gray')
    
    
    
    
######################## regla de hebb

print("\n\n regla de hebb\n\n")

"""
La regla de Hebb es una regla de aprendizaje no supervisado propuesta por Donald Hebb en 1949, 
que establece que si dos neuronas son activadas al mismo tiempo, se fortalece la conexión sináptica 
entre ellas. Esta regla establece que el cambio en la fuerza de la conexión sináptica entre dos
 neuronas depende del producto de la actividad de las neuronas.

En términos más simples, la regla de Hebb establece que cuando una célula neuronal dispara repetidamente 
y envía su señal a otra célula, la conexión entre ellas se fortalece. Esto se conoce como 
"neuronas que se activan juntas, se conectan juntas".

La aplicación práctica de la regla de Hebb es en el aprendizaje no supervisado, en el que la 
red neuronal busca patrones en los datos sin la necesidad de etiquetas de clasificación. En este 
caso, la red neuronal se entrena para reconocer patrones en los datos sin la necesidad de tener 
información previa sobre cómo se deben clasificar los datos.

En resumen, la regla de Hebb establece que la fuerza de la conexión sináptica entre dos neuronas 
se fortalece cuando ambas neuronas se activan simultáneamente, lo que puede ser utilizado en el 
aprendizaje no supervisado para buscar patrones en los datos.
"""


# Definir patrones de entrenamiento
patterns = np.array([
    [1, 1, 1, -1],      # Patrón 1
    [-1, -1, 1, 1],     # Patrón 2
    [1, -1, -1, -1],    # Patrón 3
    [-1, 1, -1, 1]      # Patrón 4
])

# Inicializar matriz de pesos con ceros
W = np.zeros((patterns.shape[1], patterns.shape[1]))

# Entrenamiento utilizando la regla de Hebb
for pattern in patterns:
    pattern = pattern.reshape(-1, 1)         # Cambia el patrón a una matriz columna
    W += np.dot(pattern, pattern.T)         # Actualiza la matriz de pesos utilizando la regla de Hebb

# Diagonal con ceros
np.fill_diagonal(W, 0)                      # Los pesos de una neurona consigo misma siempre son cero

# Función de activación
def activation(x):
    return np.where(x >= 0, 1, -1)           # Función escalón bipolar

# Prueba con patrones de entrenamiento
for pattern in patterns:
    pattern = pattern.reshape(-1, 1)         # Cambia el patrón a una matriz columna
    output = activation(np.dot(W, pattern)) # Calcula la salida utilizando la función de activación
    # Imprime el patrón de entrada y su correspondiente salida
    print(f'Entrada: {pattern.T}, Salida: {output.T}')


"""
En este ejemplo, primero definimos una matriz de patrones de entrenamiento patterns que consiste 
en 4 patrones de 4 elementos cada uno.

Luego, inicializamos la matriz de pesos W con ceros y utilizamos la regla de Hebb para entrenar 
la red neuronal, aplicando la fórmula W = W + x*x.T para cada patrón de entrenamiento. Aquí, x es
 el patrón de entrada y x.T es su transpuesta.

Después, llenamos la diagonal de la matriz W con ceros para evitar que los elementos se 
realimenten a sí mismos.

A continuación, definimos una función de activación activation que devuelve 1 para valores de 
entrada mayores o iguales a cero y -1 para valores menores que cero.

Finalmente, probamos la red neuronal con cada uno de los patrones de entrenamiento, utilizando 
la función de activación para obtener la salida de la red. El resultado se muestra en la consola 
como un par de vectores de entrada y salida.
"""

###########################   maquina de boltzman

print("\n\n maquina de boltzman\n\n")

"""
La Máquina de Boltzmann es un tipo de red neuronal artificial que se utiliza para aprender a representar 
y modelar distribuciones de probabilidad. Fue propuesta por primera vez por Geoffrey Hinton y Terry Sejnowski en 1985.

Es un modelo generativo que aprende a generar nuevos datos a partir de los datos de entrenamiento. 
Funciona mediante el uso de unidades estocásticas llamadas "neuronas" que se conectan entre sí y se 
activan o desactivan en función de los datos de entrada.

La Máquina de Boltzmann consta de dos capas: la capa visible y la capa oculta. Las unidades de la capa visible
 corresponden a las características de los datos de entrada, mientras que las unidades de la capa oculta son 
 unidades latentes que representan patrones ocultos en los datos.

El aprendizaje se realiza mediante el uso de un algoritmo de entrenamiento basado en el principio de máxima 
entropía, que busca maximizar la probabilidad de los datos de entrenamiento. Una vez que la máquina ha sido 
entrenada, puede generar nuevos datos de manera autónoma a partir de la distribución de probabilidad que ha aprendido.
"""
