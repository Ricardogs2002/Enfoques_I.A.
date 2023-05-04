# Implementación de IDDFS (Iterative Deepening Depth-First Search) 
#           (Búsqueda en profundidad iterativa)

# Definimos el grafo a buscar
graph = {'A': ['B', 'C', 'D'],
         'B': ['E', 'F'],
         'C': [],
         'D': ['G', 'H'],
         'E': [],
         'F': [],
         'G': [],
         'H': []}

# Definimos la función principal que realiza la búsqueda en profundidad iterativa
def iddfs(start, goal, max_depth):
    # Recorremos cada profundidad
    for depth in range(max_depth):
        # Almacenamos los nodos visitados en la profundidad actual
        visited = []
        # Almacenamos el camino actual
        path = []
        # Realizamos una búsqueda en profundidad limitada a la profundidad actual
        if dfs(start, goal, visited, path, depth):
            # Si encontramos el objetivo, devolvemos el camino completo
            return path + [goal]
    # Si no encontramos el objetivo en ninguna profundidad, devolvemos False
    return False

# Definimos la función auxiliar que realiza la búsqueda en profundidad limitada
def dfs(node, goal, visited, path, depth):
    # Verificamos si hemos alcanzado la profundidad límite
    if depth == 0:
        return False
    
    # Agregamos el nodo actual a la lista de visitados y al camino actual
    visited.append(node)
    path.append(node)
    
    # Verificamos si hemos encontrado el objetivo
    if node == goal:
        return True
    
    # Exploramos los nodos vecinos del nodo actual
    for neighbor in graph[node]:
        # Verificamos si el vecino no ha sido visitado antes
        if neighbor not in visited:
            # Realizamos una búsqueda en profundidad recursiva en el vecino
            if dfs(neighbor, goal, visited, path, depth - 1):
                # Si encontramos el objetivo, devolvemos True
                return True
    
    # Si no encontramos el objetivo en los vecinos del nodo actual, lo eliminamos del camino actual
    path.pop()
    # Devolvemos False para continuar la exploración en otros caminos
    return False

# Prueba de la función IDDFS
# Buscamos el camino desde el nodo 'A' hasta el nodo 'H' con una profundidad máxima de 4
print(iddfs('A', 'H', 4)) # salida: ['A', 'D', 'H']
