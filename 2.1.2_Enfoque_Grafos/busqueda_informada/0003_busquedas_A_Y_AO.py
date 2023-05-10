# busqueda A*
import heapq

def astar(start, goal, neighbors_fn, heuristic_fn, cost_fn):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}
    
    while frontier:  #Se inicia un bucle while para explorar la cola de prioridad mientras haya elementos en ella
        current_cost, current = heapq.heappop(frontier)
        
        if current == goal: # cuando el nodo actual es igual al objetivo termina el programa
            break
        # Se itera a través de los vecinos del nodo actual, y se calcula el costo actual de llegar al vecino
        for neighbor in neighbors_fn(current):
            new_cost = cost_so_far[current] + cost_fn(current, neighbor)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_fn(goal, neighbor)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current
    
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    
    return path # devolucion del camino mas corto

# Definimos los nodos y las aristas de nuestro grafo
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5, 'E': 3},
    'C': {'F': 1},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# Definimos el nodo de inicio y el objetivo
start_node = 'A'
goal_node = 'F'

# Definimos una función heurística para estimar el costo restante de llegar al objetivo desde un nodo
def heuristic(node1, node2):
    return 1  # Esta heurística siempre devuelve el mismo valor constante (1), lo que significa que no hay estimación del costo restante

# Definimos una función para obtener el costo de la arista entre dos nodos
def cost(node1, node2):
    return graph[node1][node2]

# Ejecutamos la función astar para encontrar el camino más corto desde el nodo de inicio hasta el objetivo
result = astar(start_node, goal_node, lambda n: graph[n].keys(), heuristic, cost)

# Imprimimos el resultado
print("El camino mas corto es")
print("El resutado con el metodo de busqueda A* es:", result)  # Output: ['A', 'C', 'F']


# BUSQUEDA A0*
def A0_SEARCH(graph, start_node, goal_node):
    visited = set()    # Conjunto de nodos visitados
    queue = [[start_node]]    # Cola de nodos por visitar, inicialmente contiene solo el nodo de inicio

    while queue:    # Mientras la cola no esté vacía
        path = queue.pop(0)    # Sacar el primer camino de la cola
        current_node = path[-1]    # Obtener el último nodo del camino

        if current_node == goal_node:    # Si se llegó al nodo objetivo, se devuelve el camino
            return path

        if current_node not in visited:    # Si el nodo no ha sido visitado
            visited.add(current_node)    # Se marca como visitado

           # Se imprimen el nodo actual y la cola para visualizar el proceso de búsqueda
            print(f"Nodo actual: {current_node}")
            print(f"Cola: {queue}") 

            # Se añaden a la cola los nodos vecinos del nodo actual
            for neighbor in graph[current_node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    # Si no se encontró un camino al nodo objetivo, se devuelve None
    return None


# Definimos los nodos y las aristas de nuestro grafo
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Definimos el nodo de inicio y el objetivo
start_node = 'A'
goal_node = 'F'

# Ejecutamos la función A0_SEARCH para encontrar el camino desde el nodo de inicio hasta el objetivo
result = A0_SEARCH(graph, start_node, goal_node)

# Imprimimos el resultado
print("El resultado con la busqueda A0* es: ",result)  # Output: ['A', 'C', 'F']


