

import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

# Creamos los puntos de entrenamiento. N puntos aleatorios de cada forma geometrica
N = 100  #Reducir para visualizar como afecta la calidad del resultado
circle_points = np.random.rand(N, 2) * 0.5 - 0.25
triangle_points = np.random.rand(N, 2) * 0.5 + np.array([-0.5, 0.5])
square_points = np.random.rand(N, 2) * 0.5 + np.array([0.5, -0.5])

points = np.concatenate((circle_points, triangle_points, square_points))
#, asignando el valor 0 a los puntos del círculo, 1 a los del triángulo y 2 a los del cuadrado.
labels = np.concatenate((np.zeros(N), np.ones(N), 2 * np.ones(N)))

# Creamos los puntos de prueba
M = 100
points_test = np.random.rand(M, 2) * 2 - 1

# Entrenamos el  se utiliza la información de las formas geométricas de entrada
# para entrenar un modelo que sea capaz de clasificar nuevos puntos según la forma geométrica a la que pertenecen.
clf = GaussianNB()
#mediante el método fit().
clf.fit(points, labels)

# Realizamos la prediccion
predicted_labels = clf.predict(points_test)

# Graficamos los resultados
plt.figure()

#Agrega una dispersión de puntos en la gráfica correspondiente a los puntos de la forma geometrica
# (almacenados en la variable circle_points), con etiqueta 'Circle' y color rojo ('r').
plt.scatter(circle_points[:, 0], circle_points[:, 1], label='Circle', s=10, c='r')
plt.scatter(triangle_points[:, 0], triangle_points[:, 1], label='Triangle', s=10, c='b')
plt.scatter(square_points[:, 0], square_points[:, 1], label='Square', s=10, c='g')

#Agrega una dispersión de puntos en la gráfica correspondiente a los puntos de prueba
# (almacenados en la variable points_test) y les asigna un color de acuerdo a las etiquetas
# predichas por el modelo (almacenadas en predicted_labels). La transparencia se ajusta a través del
# parámetro alpha y el tamaño de los puntos se ajusta mediante s.
plt.scatter(points_test[:, 0], points_test[:, 1], c=predicted_labels, alpha=0.2, s=100)

plt.legend()
plt.show()

