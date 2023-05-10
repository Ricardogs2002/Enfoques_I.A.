"""Es un algoritmo de optimización utilizado en inteligencia artificial y
ciencias de la computación. El objetivo de este algoritmo es encontrar
el máximo o mínimo global de una función.

El algoritmo comienza en un punto aleatorio en la función y luego evalúa
los puntos adyacentes para encontrar el punto que proporciona la mayor
mejora en la función objetivo. Este proceso se repite hasta que se 
alcanza un punto que no puede ser mejorado en ninguna direccion adyacente."""


import random

# Definimos la función principal que implementa el algoritmo de Hill Climbing
def hill_climbing(objective_function, initial_state, neighbors_function):
    current_state = initial_state  # Inicializamos el estado actual con el estado inicial
    while True:  # Iteramos hasta que se alcance una solución óptima o no se puedan encontrar más soluciones mejores
        neighbors = neighbors_function(current_state)  # Generamos los vecinos del estado actual
        print("Vecinos", neighbors)
        neighbor_values = [(neighbor, objective_function(neighbor)) for neighbor in neighbors]  # Evaluamos la función objetivo en cada vecino
        print("Valores", neighbor_values)
        best_neighbor = max(neighbor_values, key=lambda x: x[1])  # Encontramos el vecino con el valor más alto de la función objetivo
        print("Valor más alto:", best_neighbor)
        if best_neighbor[1] <= objective_function(current_state):  # Si el mejor vecino no mejora la solución actual, terminamos la búsqueda y devolvemos el estado actual
            return current_state
        current_state = best_neighbor[0]  # Si el mejor vecino mejora la solución actual, actualizamos el estado actual y continuamos buscando
        print("No es el mejor")

# Ejemplo de uso:
def objective_function(x):
    return -x**2 + 5*x + 10  # Definimos la función objetivo que queremos maximizar

def neighbors_function(x):
    return [x + random.uniform(-2, 2)]  # Generamos un nuevo punto al azar que está cerca del punto actual

initial_state = random.uniform(-10, 10)  # Generamos un estado inicial aleatorio
best_solution = hill_climbing(objective_function, initial_state, neighbors_function)  # Ejecutamos el algoritmo de Hill Climbing

print(f"La mejor solución encontrada es {best_solution} con un valor de {objective_function(best_solution)}")  # Mostramos la mejor solución encontrada y su valor de la función objetivo

