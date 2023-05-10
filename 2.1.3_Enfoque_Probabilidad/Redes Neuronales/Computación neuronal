# Importar TensorFlow y Keras
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# Cargar conjunto de datos de imágenes de MNIST
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Preprocesar datos
# Redimensionar imágenes y convertir píxeles de 0-255 a 0-1
X_train = X_train.reshape(-1, 28*28).astype("float32") / 255.0
X_test = X_test.reshape(-1, 28*28).astype("float32") / 255.0

# Codificar etiquetas como one-hot
y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)

# Crear modelo de red neuronal
# Crear una secuencia de capas de neuronas
# En este caso, estamos usando una red neuronal completamente conectada (Dense) con tres capas ocultas
# La primera capa oculta tiene 256 neuronas y la función de activación ReLU
# La segunda capa oculta tiene 128 neuronas y la función de activación ReLU
# La capa de salida tiene 10 neuronas (una para cada dígito del 0 al 9) y la función de activación softmax
model = keras.Sequential([
    layers.Dense(256, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compilar modelo
# Configurar modelo para entrenamiento con la función de pérdida y el optimizador
# En este caso, estamos utilizando la función de pérdida de entropía cruzada categórica y el optimizador Adam
# También estamos haciendo un seguimiento de la precisión como una métrica de evaluación durante el entrenamiento
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar modelo
# Alimentar datos al modelo para que aprenda de ellos
# En este caso, estamos entrenando el modelo durante 5 épocas (pasadas completas a través del conjunto de entrenamiento)
# y utilizando un tamaño de lote (batch size) de 32 (es decir, actualizando los pesos después de procesar 32 imágenes a la vez)
model.fit(X_train, y_train, epochs=5, batch_size=32)

# Evaluar modelo
# Evaluar el rendimiento del modelo en datos de prueba
# En este caso, estamos calculando la pérdida y la precisión del modelo en el conjunto de prueba
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Precisión de prueba:", test_acc)

"""
La computación neuronal es un enfoque en la 
inteligencia artificial (IA) que está inspirado 
en el cerebro humano y su funcionamiento. En lugar 
de programar una computadora para realizar tareas 
específicas, la computación neuronal utiliza redes 
neuronales artificiales (ANN, por sus siglas en inglés) 
para aprender a realizar tareas a través de la experiencia.
"""
