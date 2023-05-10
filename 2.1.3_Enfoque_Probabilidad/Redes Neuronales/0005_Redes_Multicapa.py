import tensorflow as tf
import numpy as np

# Datos de entrenamiento
X = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = np.array([[0], [1], [1], [0]])

# Parámetros de la red neuronal
n_input = 3
n_hidden1 = 4
n_hidden2 = 4
n_output = 1

# Modelo de la red neuronal
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(n_hidden1, input_shape=(n_input,), activation='relu'),
    tf.keras.layers.Dense(n_hidden2, activation='relu'),
    tf.keras.layers.Dense(n_output, activation='sigmoid')
])

# Compilamos el modelo
modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo
modelo.fit(X, y, epochs=1000, verbose=0)
