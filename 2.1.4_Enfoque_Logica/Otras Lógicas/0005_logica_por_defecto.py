# Importar la biblioteca NumPy
import numpy as np

# Definir las variables lógicas
variables = ["p", "q"]

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

# Ejemplo de uso
formula = "p and q"

# Calcular la lista de valores de la fórmula para cada combinación de valores lógicos
valores_formula = []
for i in range(num_combinaciones):
    valores_formula.append(evaluar_formula(formula, combinaciones[i,:]))

# Imprimir la tabla de verdad de la fórmula
print("Tabla de verdad de la fórmula", formula)
for i in range(num_combinaciones):
    for j in range(len(variables)):
        print(combinaciones[i,j], end="")
    print(":", valores_formula[i])

#

#La lógica por defecto en Python se refiere al conjunto de operaciones lógicas y de comparación que están disponibles en el lenguaje de programación
#por defecto. Estas operaciones permiten evaluar condiciones y tomar decisiones en función de ellas en un programa.

#Algunas de las operaciones lógicas y de comparación disponibles en Python son:

#and: devuelve True si ambas condiciones son verdaderas.
#or: devuelve True si al menos una de las condiciones es verdadera.
#not: devuelve el valor opuesto de una condición.
#==: devuelve True si dos valores son iguales.
#!=: devuelve True si dos valores son diferentes.
#<: devuelve True si el primer valor es menor que el segundo.
#>: devuelve True si el primer valor es mayor que el segundo.
#<=: devuelve True si el primer valor es menor o igual que el segundo.
#>=: devuelve True si el primer valor es mayor o igual que el segundo.
