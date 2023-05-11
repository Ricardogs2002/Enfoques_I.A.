import numpy as np

# Crear un conjunto de datos aleatorio
X = np.random.randn(5)

# Definir la función de activación ReLU
# La funcion relu hace que los valores negativos se hagan 0 y los valores positivos se mantengan sin cambio
def relu(x):
    return np.maximum(0, x)

# Definir la función de activación Sigmoid.
#La funcion sigmoid reasigna todos los valores a numeros decimales entre el 0-1 lo cual es util para verlos como una probabilidad
#esta funcion asigna valores cercanos a 1 si los valores originales son grandes positivos y viceversa
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Definir la función de activación Softmax
#Softmax reasigna los valores para que la suma de todos estos sea igual a 1 por lo que al igual que softmax...
#asigna valores cercanos a 1 si los valores originales son grandes positivos y viceversa
def softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)

# Calcular los resultados de las funciones de activación
relu_result = relu(X)
sigmoid_result = sigmoid(X)
softmax_result = softmax(X)

# Mostrar los resultados en una sola línea
print("Valores de entrada:", X)
print("ReLU:", relu_result.flatten())
print("Sigmoid:", sigmoid_result.flatten())
print("Softmax:", softmax_result.flatten())

