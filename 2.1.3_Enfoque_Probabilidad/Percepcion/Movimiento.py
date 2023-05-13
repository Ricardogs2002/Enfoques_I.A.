"""
El algoritmo de movimiento basado en la probabilidad es una técnica utilizada en inteligencia artificial y 
robótica para permitir que un robot se mueva de manera autónoma en un entorno desconocido.
En este algoritmo, el robot utiliza sensores para obtener información sobre su entorno y crea un 
mapa del mismo. Luego, el robot utiliza este mapa para calcular la probabilidad de que se encuentre en una 
ubicación específica y la probabilidad de que se mueva en una dirección determinada
"""
import random
import matplotlib.pyplot as plt

# Definir el tamaño del entorno
size_x = 10
size_y = 10

# Definir la posición inicial del robot
start_x = random.randint(0, size_x-1)
start_y = random.randint(0, size_y-1)

# Crear el mapa del entorno
environment = [[0] * size_x for _ in range(size_y)]
environment[start_y][start_x] = 1

# Función para mostrar el mapa del entorno
def plot_environment():
    plt.imshow(environment, cmap='Blues', interpolation='nearest')
    plt.xticks(range(size_x))
    plt.yticks(range(size_y))
    plt.grid(color='black', lw=0.5)
    plt.show()

# Mostrar el entorno inicial
plot_environment()

# Definir la función de movimiento basado en la probabilidad
def move():
    current_x, current_y = start_x, start_y

    while True:
        # Calcular las probabilidades de movimiento
        probabilities = []
        total_probability = 0

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = current_x + dx, current_y + dy

            if 0 <= new_x < size_x and 0 <= new_y < size_y:
                probability = random.random()
                probabilities.append((probability, new_x, new_y))
                total_probability += probability

        # Normalizar las probabilidades
        probabilities = [(prob / total_probability, new_x, new_y) for prob, new_x, new_y in probabilities]

        # Seleccionar una dirección basada en las probabilidades
        selected_probability = random.random()
        cumulative_probability = 0

        for probability, new_x, new_y in probabilities:
            cumulative_probability += probability

            if selected_probability <= cumulative_probability:
                current_x, current_y = new_x, new_y
                environment[current_y][current_x] += 1
                break

        # Mostrar el entorno actualizado
        plot_environment()

# Ejecutar el algoritmo de movimiento basado en la probabilidad
move()
""""
Este programa crea un entorno bidimensional y un robot que se mueve en el mismo. En cada paso, 
el robot calcula las probabilidades de movimiento en las direcciones disponibles y selecciona una
dirección basada en esas probabilidades. El entorno se visualiza utilizando la biblioteca matplotlib.
