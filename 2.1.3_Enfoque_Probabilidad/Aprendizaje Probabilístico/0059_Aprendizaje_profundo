#Implementación de aprendizaje profundo (deep learning)

import matplotlib.pyplot as plt
from tensorflow import keras


# Cargar el conjunto de datos MNIST
# Cada imagen del conjunto de datos MNIST es una imagen en escala de grises de 28x28 píxeles de un dígito manuscrito 
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Preprocesar los datos
# Reshape: cada imagen se aplana en un vector de 784 elementos (28x28) para poder ser procesada por la red neuronal
x_train = x_train.reshape((60000, 28 * 28)) / 255.0 # Normalización de los valores de píxel al rango [0, 1]
x_test = x_test.reshape((10000, 28 * 28)) / 255.0
y_train = keras.utils.to_categorical(y_train) # Convertir las etiquetas a un formato one-hot
y_test = keras.utils.to_categorical(y_test)

# Construir la red neuronal
model = keras.models.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(28 * 28,)), # Capa de entrada: 784 neuronas (una por cada píxel), activación relu
    keras.layers.Dense(10, activation='softmax') # Capa de salida: 10 neuronas (una por cada dígito), activación softmax
])

# Compilar el modelo
# optimizer: algoritmo de optimización del modelo, que en este caso es rmsprop
# loss: función de pérdida que mide cómo de mal está prediciendo el modelo, que en este caso es categorical_crossentropy
# metrics: métricas que se utilizan para evaluar el modelo, en este caso la precisión (accuracy)
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo
# epochs: número de veces que se entrena el modelo con el conjunto de datos
# batch_size: número de muestras que se utilizan para calcular la función de pérdida antes de actualizar los pesos del modelo
history = model.fit(x_train, y_train, epochs=5, batch_size=64)

# Evaluar el modelo en los datos de prueba
test_loss, test_acc = model.evaluate(x_test, y_test)
print('Precision del Test:', test_acc)

# Visualizar algunas imágenes de ejemplo
for i in range(5):
    plt.imshow(x_test[i].reshape(28,28), cmap='gray') # Mostrar la imagen
    plt.show()
