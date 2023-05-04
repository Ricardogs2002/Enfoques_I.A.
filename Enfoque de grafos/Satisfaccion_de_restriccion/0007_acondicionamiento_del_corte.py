# Implementación del algoritmo de Edmonds-Karp con acondicionamiento del corte
# Este código es una tecnica que se utiliza para mejorar la eficiencia del algoritmo de Edmonds-Karp, que es el que tome de ejemplo


# Función para encontrar el flujo máximo en un grafo utilizando el algoritmo de Edmonds-Karp con acondicionamiento del corte
# Los parámetros de entrada son el grafo de capacidad (graph), el nodo de origen (source) y el nodo de destino (sink)
def edmonds_karp_cut_conditioning(graph, source, sink):
    # Inicializar el flujo máximo en 0
    max_flow = 0
    
    # Mientras haya un camino de aumento en el grafo
    while True:
        # Encontrar un camino de aumento usando BFS (busqueda de anchura) desde el nodo origen hasta el nodo destino
        path, flow = bfs_find_path(graph, source, sink)
        
        # Si no hay más caminos de aumento, terminar
        if not path:
            break
        
        # Actualizar el flujo máximo
        max_flow += flow
        
        # Acondicionar el corte
        for u, v in get_cut(graph, path):
            # Si el corte no está saturado
            if graph[u][v] > 0:
                # Reducir el corte
                #La capacidad de la arista en dirección original se reduce a cero
                graph[u][v] = 0
                #Se incrementa la capacidad de la arista en la dirección opuesta
                graph[v][u] += graph[u][v]
    
    return max_flow

# Función para encontrar un camino de aumento utilizando BFS (busqueda de anchura)
def bfs_find_path(graph, source, sink):
    # Inicializar la cola de nodos
    queue = [(source, [source], float('inf'))]
    
    # Mientras haya nodos en la cola
    while queue:
        # Obtener el siguiente nodo de la cola
        node, path, flow = queue.pop(0)
        
        # Si se llegó al nodo destino, terminar
        if node == sink:
            return path, flow
        
        # Recorrer los nodos adyacentes
        for neighbor in graph[node]:
            # Si el nodo adyacente no está en el camino y hay capacidad disponible
            if neighbor not in path and graph[node][neighbor] > 0:
                # Calcular el flujo mínimo a través del camino
                new_flow = min(flow, graph[node][neighbor])
                
                # Agregar el nodo adyacente al camino y actualizar el flujo
                # Se utiliza para crear un nuevo camino que incluye al nodo adyacente que se está examinando
                new_path = path + [neighbor]
                # Se utiliza para determinar la capacidad disponible para el nuevo camino
                new_flow = min(flow, graph[node][neighbor])
                
                # Agregar el nodo adyacente a la cola
                queue.append((neighbor, new_path, new_flow))
    
    # Si no se encontró un camino de aumento, devolver None
    return None, 0

# Función para obtener el flujo de un camino en el grafo
def get_path_flow(graph, path):
    # Inicializar el flujo en infinito
    flow = float('inf')
    
    # Recorrer los nodos en el camino y actualizar el flujo
    for i in range(len(path)-1):
        # Se utilizan para obtener los nodos que están conectados por la arista que se está examinando en el camino de aumento
        u, v = path[i], path[i+1]
        # Se calcula la capacidad disponible a lo largo de esa arista. Esto se hace utilizando la función min
        flow = min(flow, graph[u][v])
    
    return flow

# Función para obtener el corte en el grafo a partir de un camino de aumento
# Esta función utiliza el algoritmo de búsqueda en anchura (BFS) (busqueda de anchura) para encontrar un corte mínimo que 
# separe el nodo de origen (source) del nodo de destino (sink). 
def get_cut(graph, path):
    # Inicializar el corte como un conjunto vacío
    cut = set()
    
    # Recorrer los nodos en el camino y agregar las aristas al corte
    for i in range(len(path)-1):
        u, v = path[i], path[i+1]
        # El conjunto en cuestión es el corte mínimo encontrado en el grafo. 
        #Se usa para comprobar si se han explorado todos los posibles cortes en el grafo.
        cut.add((u, v))
    
    # Agregar las aristas del corte que no están saturadas
    return [(u, v) for u, v in cut if graph[u][v] > 0]
