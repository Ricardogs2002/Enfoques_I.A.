
from queue import PriorityQueue

# Define la función para la búsqueda en anchura de costo uniforme
def bfs_costo_uniforme(nodo_inicial, nodo_objetivo, grafo):
    # Inicializa una cola de prioridad y agrega el nodo inicial con un costo de 0
    cola_prioridad = PriorityQueue()
    cola_prioridad.put((0, [nodo_inicial]))
    
    while not cola_prioridad.empty():
        # Saca el elemento con menor costo de la cola de prioridad
        (costo, camino) = cola_prioridad.get()
        # Obtiene el nodo más reciente del camino
        nodo_actual = camino[-1]
        
        # Verifica si se ha llegado al nodo objetivo
        if nodo_actual == nodo_objetivo:
            return camino
        
        # Recorre los vecinos del nodo actual y los agrega a la cola de prioridad
        for vecino, costo_vecino in grafo[nodo_actual].items():
            # Verifica que el vecino no esté ya en el camino
            if vecino not in camino:
                # Calcula el costo acumulado del nuevo camino
                costo_nuevo_camino = costo + costo_vecino
                # Crea el nuevo camino y lo agrega a la cola de prioridad
                nuevo_camino = camino + [vecino]
                cola_prioridad.put((costo_nuevo_camino, nuevo_camino))
    
    # Si no se encontró un camino al nodo objetivo, devuelve None
    return None

# Ejemplo de uso
grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3}
}

camino = bfs_costo_uniforme('A', 'E', grafo)
print(camino)
