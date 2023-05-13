
#Perceptrone Adaline y Madaline "ADALINE"

#Practicamente son lo mismo, solo que el adeline es una red neuronal de 1 sola capa
#y el madeline funciona con multiples capas

import numpy as np

class Adaline:
    def __init__(self, learning_rate=0.01, epochs=50):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        #Inicializa los pesos y el sesgo aleatoriamente
        self.weights = np.random.randn(X.shape[1])
        self.bias = np.random.randn()

        for _ in range(self.epochs):
            #Calcula la salida y la diferencia de error
            output = self.predict(X)
            error = y - output

            #Actualiza los pesos y el sesgo
            self.weights += self.learning_rate * np.dot(X.T, error)
            self.bias += self.learning_rate * np.sum(error)

    def predict(self, X):
        #Calcula la salida
        return np.dot(X, self.weights) + self.bias

#Datos de entrenamiento
X = np.array([[0.5, 0.2],
              [0.3, 0.8],
              [0.9, 0.5],
              [0.1, 0.9]])
y = np.array([0.4, 0.6, 0.8, 0.2])

#Crea y entrena el modelo Adaline
model = Adaline(learning_rate=0.01, epochs=100)
model.fit(X, y)

#Datos de prueba
X_test = np.array([[0.4, 0.3],
                   [0.7, 0.6]])

#Realiza predicciones
predictions = model.predict(X_test)
print("Predicciones:", predictions)
