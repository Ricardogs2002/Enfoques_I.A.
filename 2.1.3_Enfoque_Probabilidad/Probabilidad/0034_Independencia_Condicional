# Areli Sarai García Medina | 20310380
# Independencia Codicional

# Queremos tirar dos dados con resultados independientes (variable 'a' y 'b'), pero que al tener una variable extra 'c' se hagan dependientes

# Importamos la biblioteca random para simular los dados
import random

# Definimos las dos variables aleatorias X y Y (tirada del dado 1 y 2)
X = [1, 2, 3, 4, 5, 6]
Y = [1, 2, 3, 4, 5, 6]

# Definimos la función para simular una tirada de dado
def tirar_dado():
    return random.randint(1, 6)

# Definimos la matriz de probabilidad conjunta P(X,Y)
P_XY = [[0 for j in range(len(Y))] for i in range(len(X))]
for i in range(len(X)):
    for j in range(len(Y)):
        P_XY[i][j] = 1/36

# Calculamos las distribuciones marginales P(X) y P(Y)
P_X = [1/6 for i in range(len(X))]
P_Y = [1/6 for i in range(len(Y))]

# Simulamos dos tiradas de dado
x = tirar_dado()
y = tirar_dado()

# Calculamos la independencia condicional P(X|Y)
P_X_given_Y = [[0 for j in range(len(Y))] for i in range(len(X))]
for i in range(len(X)):
    for j in range(len(Y)):
        P_X_given_Y[i][j] = P_XY[i][j] / P_Y[j]

# Imprimimos los resultados
print("La primera tirada del dado fue:", x)
print("La segunda tirada del dado fue:", y)
print("La probabilidad conjunta de que la primera tirada sea", x, "y la segunda tirada sea", y, "es", P_XY[x-1][y-1])
print("La probabilidad marginal de que la primera tirada sea", x, "es", P_X[x-1])
print("La probabilidad marginal de que la segunda tirada sea", y, "es", P_Y[y-1])
print("La probabilidad condicional de que la primera tirada sea", x, "dado que la segunda tirada es", y, "es", P_X_given_Y[x-1][y-1])
