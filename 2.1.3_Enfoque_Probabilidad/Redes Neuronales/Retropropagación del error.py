"""La retropropagación del error (backpropagation en inglés) es un algoritmo
utilizado en el aprendizajesupervisado de redes neuronales artificiales para
entrenar los pesos de las conexiones entre neuronas.

En términos simples, el objetivo del algoritmo de retropropagación es ajustar
los pesos de la red neuronal para que la salida de la red se acerque lo más
posible a la salida deseada para un conjunto de datos de entrenamiento dado.

El algoritmo funciona en dos fases: propagación hacia adelante y propagación hacia atrás.

Durante la fase de propagación hacia adelante, se proporciona un conjunto de
datos de entrada a la red neuronal y se calcula la salida de la red. Luego,
se compara la salida de la red con la salida deseada y se calcula un error.

En la fase de propagación hacia atrás, se utiliza el error calculado en la
fase anterior para ajustar los pesos de la red neuronal. El error se propaga
hacia atrás a través de la red, de la capa de salida a la capa de entrada,
para calcular la contribución de cada peso en el error. Luego, se utiliza
esta información para ajustar los pesos de la red de manera que la salida de
la red se acerque más a la salida deseada en el siguiente ciclo de entrenamiento.

El proceso se repite para múltiples ciclos de entrenamiento hasta que la red
neuronal se ajuste adecuadamente a los datos de entrenamiento. Una vez
entrenada, la red neuronal se puede utilizar para predecir la salida de
nuevos conjuntos de datos de entrada."""

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
import numpy as np

# Generamos datos de ejemplo
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) # entradas
y = np.array([0, 1, 1, 0]) # salidas deseadas

# Definimos la arquitectura de la red neuronal
model = Sequential() # modelo secuencial
model.add(Dense(2, input_dim=2, activation='sigmoid')) # capa densa con 2 neuronas y función de activación sigmoidal
model.add(Dense(1, activation='sigmoid')) # capa de salida con 1 neurona y función de activación sigmoidal

# Compilamos el modelo
sgd = SGD(lr=0.1) # optimizador SGD con tasa de aprendizaje 0.1
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy']) # compilamos el modelo con función de pérdida de entropía cruzada binaria y métrica de precisión

# Entrenamos el modelo
model.fit(X, y, epochs=1000, verbose=0) # entrenamos el modelo con los datos de entrada X y las salidas deseadas y durante 1000 épocas

# Evaluamos el modelo entrenado
scores = model.evaluate(X, y) # evaluamos el modelo en los mismos datos de entrada y salidas deseadas para ver la precisión
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100)) # mostramos la precisión del modelo

