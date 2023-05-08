import networkx as nx
import random
import matplotlib.pyplot as plt

def local_beam_search(graph, start_node, beam_width, goal_node):
    current_nodes = [start_node]
    
    while True:
        next_nodes = []
        for node in current_nodes:
            if node == goal_node:
                return node
            
            neighbors = list(graph.neighbors(node))
            if not neighbors:
                continue
            
            if len(neighbors) <= beam_width:
                next_nodes += neighbors
            else:
                sorted_neighbors = sorted([(neighbor, graph.degree(neighbor)) for neighbor in neighbors],
                                          key=lambda x: -x[1])
                next_nodes += [neighbor for neighbor, _ in sorted_neighbors[:beam_width]]
                
        if not next_nodes:
            return None
        
        current_nodes = next_nodes
        random.shuffle(current_nodes)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un grafo aleatorio
    G = nx.erdos_renyi_graph(10, 0.3)
    start_node = 0
    goal_node = 9
    beam_width = 3
    
    # Ejecutar la búsqueda de haz local
    result = local_beam_search(G, start_node, beam_width, goal_node)
    
    # Graficar el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    
    # Resaltar el camino encontrado
    if result is not None:
        path = nx.shortest_path(G, start_node, result)
        edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2.0)
        
    # Mostrar el resultado
    if result is not None:
        print(f"Se encontró un camino desde el nodo {start_node} al nodo {goal_node}: {path}")
    else:
        print(f"No se encontró un camino desde el nodo {start_node} al nodo {goal_node} utilizando una búsqueda de haz local con ancho de haz {beam_width}")
    
    plt.show()
    
#Teoria    
"""
La búsqueda de haz local en grafos es una técnica de búsqueda heurística que se utiliza para encontrar una solución aproximada a un problema de búsqueda en un grafo. 
Esta técnica se basa en mantener un conjunto de nodos candidatos (el "haz") y expandirlos de manera selectiva en cada iteración de la búsqueda.
En cada iteración, se seleccionan los nodos más prometedores (según una heurística determinada) para expandirlos y generar nuevos candidatos.

El proceso comienza con un conjunto inicial de nodos candidatos, que generalmente se seleccionan de forma aleatoria o según algún criterio heurístico.
A continuación, se expanden los nodos candidatos y se generan nuevos nodos candidatos. 
El proceso de expansión puede continuar hasta que se encuentra una solución o se alcanza un criterio de parada (por ejemplo, un límite en el número de iteraciones).
""" 
