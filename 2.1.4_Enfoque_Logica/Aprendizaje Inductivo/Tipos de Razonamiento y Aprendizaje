#En IA la adaptacion se puede dar gracias a la implementacion de un algoritmo de aprendizaje
#Aunque hay muchos tipos de aprendizaje en este codigo se muestra la implementacion de un algoritmo de aprendizaje supervisado
#Esto gracias a la regresion lineal, la cual nos traduce un sistema en una ecuacion lineal para poder predecir los valores siguientes
import matplotlib.pyplot as plt

# Datos de entrada de ambos ejes
X = [[1], [2], [3], [4], [5]]
y = [1, 3, 4, 7, 8]

# Calcular promedios
n = len(X)
#Se calculan los promedios
x_prom = sum([X[i][0] for i in range(n)]) / n
y_prom = sum(y) / n

# Calcular coeficientes
numerator = 0
denominator = 0
for i in range(n):
    #Se calcula la diferencia entre los valores de X y Y de su promedio 
    numerator += (X[i][0] - x_prom) * (y[i] - y_prom)
    denominator += (X[i][0] - x_prom) ** 2
#Se calcula el coeficiente de regresion 1 dividiendo el numerador subre el denominador
b1 = numerator / denominator
#Se calcula el coeficiente de regresion 2 ,    y = b0 + b1 * X
b0 = y_prom - (b1 * x_prom)

# Predecir valores para nuevos datos
#Se crea una lista para guardar las predicciones
y_pred = []
for xi in [[6], [7], [8]]:
    y_pred.append(b0 + (b1 * xi[0]))

# Graficar resultados
plt.scatter(X, y)
plt.plot(X + [[6], [7], [8]], y + y_pred, c='r')
plt.show()
