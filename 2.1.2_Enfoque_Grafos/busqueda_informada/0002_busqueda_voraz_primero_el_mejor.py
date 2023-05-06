import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

# Creamos el grafo no dirigido
G = nx.Graph()
G.add_edges_from([('A', 'B', {'weight': 4}), ('A', 'C', {'weight': 1}), ('B', 'C', {'weight': 2}), ('B', 'D', {'weight': 5}), ('C', 'D', {'weight': 1}), ('C', 'E', {'weight': 6}), ('D', 'E', {'weight': 3})])

# Implementamos la función gbfs
def gbfs(G, start, end):
    visited = set()  # Conjunto de nodos visitados
    pq = PriorityQueue()  # Cola de prioridad para los nodos
    pq.put((0, start))  # Agregamos el nodo de inicio con una prioridad de 0
    while not pq.empty():  # Mientras la cola no esté vacía
        node = pq.get()[1]  # Obtenemos el nodo con la menor prioridad
        if node == end:  # Si encontramos el nodo objetivo
            return visited  # Regresamos el conjunto de nodos visitados
        if node not in visited:  # Si el nodo no ha sido visitado aún
            visited.add(node)  # Lo agregamos al conjunto de nodos visitados
            for neighbor in G.neighbors(node):  # Para cada vecino del nodo actual
                if neighbor not in visited:  # Si el vecino no ha sido visitado aún
                    pq.put((G[node][neighbor]['weight'], neighbor))  # Agregamos el vecino a la cola de prioridad con su peso como prioridad
    return None  # Si no encontramos el nodo objetivo, regresamos None

# Llamamos a la función gbfs con el nodo de inicio y el nodo objetivo
path = gbfs(G, 'A', 'E')
if path is not None:  # Si se encontró un camino
    print("El camino más corto es:", list(path))  # Imprimimos el camino más corto
else:  # Si no se encontró un camino
    print("No se encontró un camino")

# Visualizamos el grafo y el camino encontrado
nx.draw(G, with_labels=True)  # Dibujamos el grafo
nx.draw_networkx_edges(G, nx.path_graph(path), edge_color='r', width=5)  # Dibujamos el camino más corto en rojo
plt.show()  # Mostramos la figura

"""
La Búsqueda Voraz Primero el Mejor es un algoritmo de búsqueda heurística que se utiliza para encontrar el camino más corto entre 
dos nodos en un grafo ponderado. A diferencia del algoritmo de Dijkstra, que usa una función de coste para determinar el camino más 
corto, el GBFS utiliza una heurística para guiar la búsqueda hacia el nodo objetivo.

El GBFS es similar al algoritmo de Búsqueda en Anchura (BFS, por sus siglas en inglés), en el sentido de que comienza en un nodo de inicio y
explora el grafo en capas, pero en lugar de expandir todos los nodos en la siguiente capa, el GBFS elige el nodo que se acerca más al objetivo, 
según la heurística elegida. La heurística es una función que estima cuánto falta para llegar al objetivo, y se utiliza para ordenar los nodos que 
se agregan a la lista de prioridad.

El algoritmo funciona de la siguiente manera:

Agregar el nodo de inicio a una cola de prioridad, con una prioridad de 0.
Mientras la cola de prioridad no esté vacía:
Extraer el nodo con la menor prioridad de la cola de prioridad.
Si el nodo es el objetivo, regresar el camino hasta el nodo de inicio.
Si el nodo no ha sido visitado:
Marcar el nodo como visitado.
Para cada vecino del nodo actual:
Si el vecino no ha sido visitado, agregarlo a la cola de prioridad con la heurística como prioridad.
La heurística elegida es importante, ya que determina la eficacia del algoritmo. Una heurística perfecta proporcionaría una solución óptima, 
pero es difícil encontrar una heurística perfecta para la mayoría de los problemas. La heurística utilizada en este ejemplo es simplemente la 
distancia en línea recta entre el nodo actual y el objetivo (en el caso de un grafo no dirigido), lo que se conoce como la heurística de la distancia euclidiana.

En resumen, el GBFS es un algoritmo de búsqueda heurística que utiliza una heurística para guiar la búsqueda hacia el nodo objetivo. Es similar al algoritmo 
BFS, pero en lugar de expandir todos los nodos en la siguiente capa, el GBFS elige el nodo que se acerca más al objetivo según la heurística elegida. 
La heurística elegida es importante y determina la eficacia del algoritmo.
