
#Perceptrone Adaline y Madaline "MADALINE"

#Practicamente son lo mismo, solo que el adeline es una red neuronal de 1 sola capa
#y el madeline funciona con multiples capas

#Este programa resuelve un problema de clasificacion binaria

import numpy as np

class Madaline:
    def __init__(self, num_layers, layer_size, learning_rate=0.01, epochs=50):
        self.num_layers = num_layers
        self.layer_size = layer_size
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None

    def fit(self, X, y):
        #Inicializa los pesos aleatoriamente
        self.weights = [np.random.randn(X.shape[1], self.layer_size)]
        self.weights += [np.random.randn(self.layer_size, self.layer_size) for _ in range(self.num_layers - 1)]

        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                #Propagación hacia adelante
                outputs = [xi]
                for i in range(self.num_layers):
                    net_input = np.dot(outputs[i], self.weights[i])
                    output = self._linear_activation(net_input)
                    outputs.append(output)

                #Retropropagación del error y ajuste de los pesos
                errors = [target - outputs[-1]]
                for i in range(self.num_layers - 1, 0, -1):
                    error = np.dot(errors[0], self.weights[i].T)
                    errors.insert(0, error)
                    delta = self.learning_rate * errors[0] * self._linear_derivative(outputs[i])
                    self.weights[i] += outputs[i].reshape(-1, 1) @ delta.reshape(1, -1)

    def predict(self, X):
        #Propagación hacia adelante para realizar predicciones
        outputs = [X]
        for i in range(self.num_layers):
            net_input = np.dot(outputs[i], self.weights[i])
            output = self._linear_activation(net_input)
            outputs.append(output)

        return np.where(outputs[-1] >= 0.5, 1, 0)

    def _linear_activation(self, x):
        return x

    def _linear_derivative(self, x):
        return 1

#Datos de entrenamiento
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])

#Crea y entrenar el modelo Madaline
model = Madaline(num_layers=2, layer_size=2, learning_rate=0.01, epochs=100)
model.fit(X, y)

#Datos de prueba
X_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

#Realiza predicciones
predictions = model.predict(X_test)
print("Predicciones:", predictions)
