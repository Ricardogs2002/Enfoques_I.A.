import matplotlib.pyplot as plt

# Datos de entrada
X = [[1], [2], [3], [4], [5]]
y = [1, 3, 4, 7, 8]

# Calcular promedios
n = len(X)
x_mean = sum([X[i][0] for i in range(n)]) / n
y_mean = sum(y) / n

# Calcular coeficientes
numerator = 0
denominator = 0
for i in range(n):
    numerator += (X[i][0] - x_mean) * (y[i] - y_mean)
    denominator += (X[i][0] - x_mean) ** 2
b1 = numerator / denominator
b0 = y_mean - (b1 * x_mean)

# Predecir valores para nuevos datos
y_pred = []
for xi in [[6], [7], [8]]:
    y_pred.append(b0 + (b1 * xi[0]))

# Graficar resultados
plt.scatter(X, y)
plt.plot(X + [[6], [7], [8]], y + y_pred, c='r')
plt.show()
