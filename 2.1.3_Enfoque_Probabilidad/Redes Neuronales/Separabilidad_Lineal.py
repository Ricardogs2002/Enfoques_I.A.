import tensorflow as tf

# Definir la red neuronal
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),
    tf.keras.layers.Dense(4, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilar el modelo
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo
history = model.fit(X, y, epochs=100, verbose=0)

# Graficar la frontera de decisión
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.5)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title("Frontera de decisión de la red neuronal")
plt.show()
"""
Este código definirá una red neuronal con una capa oculta de cuatro neuronas y una capa de salida de una neurona 
con función de activación sigmoide. Luego, entrenará la red neuronal en los datos generados aleatoriamente utilizando 
el optimizador Adam y la función de pérdida de entropía cruzada binaria. Finalmente, se graficará la frontera de decisión 
de la red neuronal, que separará las dos clases utilizando una línea recta.

El resultado final será un gráfico con los datos aleatorios y la frontera de decisión de la red neuronal, que separa las 
dos clases de manera lineal.
