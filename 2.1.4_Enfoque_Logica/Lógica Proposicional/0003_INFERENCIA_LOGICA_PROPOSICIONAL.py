# Importar la biblioteca NumPy
import numpy as np

# Definir las variables lógicas
variables = ["p", "q", "r"]

# Calcular el número de combinaciones posibles de valores lógicos
num_combinaciones = 2 ** len(variables)

# Crear una matriz para almacenar las combinaciones de valores lógicos
combinaciones = np.zeros((num_combinaciones, len(variables)), dtype=int)

# Llenar la matriz con todas las combinaciones posibles de valores lógicos
for i in range(num_combinaciones):
    for j in range(len(variables)):
        if i % 2**j >= 2**(j-1):
            combinaciones[i,j] = 1

# Definir una función para evaluar una fórmula lógica
def evaluar_formula(formula, valores):
    for i in range(len(variables)):
        formula = formula.replace(variables[i], str(valores[i]))
    resultado = eval(formula)
    return resultado

# Definir una función para calcular la tabla de verdad de una fórmula lógica
def tabla_verdad(formula):
    valores = []
    for i in range(num_combinaciones):
        valores.append(evaluar_formula(formula, combinaciones[i,:]))
    return valores

# Ejemplo de uso
formula = "p & q"
resultado = tabla_verdad(formula)

# Imprimir la tabla de verdad
print("Tabla de verdad de la fórmula", formula)
for i in range(num_combinaciones):
    for j in range(len(variables)):
        print(combinaciones[i,j], end="")
    print(":", resultado[i])

# Comprobar si la fórmula es una tautología
tautologia = all(resultado)

# Imprimir el resultado de la comprobación
if tautologia:
    print("La fórmula es una tautología.")
else:
    print("La fórmula no es una tautología.")
