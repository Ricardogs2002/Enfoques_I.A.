import networkx as nx
import matplotlib.pyplot as plt

#La red jerárquica de tareas (denominada también del inglés como: Hierarchical task network o
#abreviadamente HTN) es un algoritmo de planificación automática que crea 
#un plan por descomposición de tareas en subtareas hasta lograr primitivas que pueden
# ser ejecutadas directamente. La dependencia entre las acciones se proporciona en 
#forma de red (Network). La descomposición se aplica en cumplimiento de unas precondiciones 
#según una jerarquía.

# Define los operadores primitivos
def visitar_nodo(nodo):
    print("Visitando nodo:", nodo)

def realizar_accion(accion):
    print("Realizando acción:", accion)

# Define los métodos HTN(Hierarchical task network)
def explorar_grafo(grafo, nodo_actual, nodo_objetivo):
    if nodo_actual == nodo_objetivo:
        return (visitar_nodo, nodo_actual)
    else:
        vecinos = grafo[nodo_actual]
        subtareas = []
        for vecino in vecinos:
            subtareas.append((explorar_grafo, grafo, vecino, nodo_objetivo))
        return subtareas

def ejecutar_tarea(tarea, G):
    pila = [tarea]
    while pila:
        tarea_actual = pila[-1]
        if callable(tarea_actual):
            tarea_actual()
            pila.pop()
        elif isinstance(tarea_actual, tuple):
            metodo, *argumentos = tarea_actual
            print("Viaje de", argumentos[-2], "a", argumentos[-1])
            nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
            camino = nx.shortest_path(G, argumentos[-2], argumentos[-1])
            colores_aristas = ['r' if (camino[i], camino[i+1]) in G.edges() else 'black' for i in range(len(camino)-1)]
            nx.draw_networkx_edges(G, pos=pos, edgelist=[(camino[i], camino[i+1]) for i in range(len(camino)-1)], edge_color=colores_aristas, width=2)
            plt.show()
            resultado = metodo(*argumentos)
            pila.pop()
            if isinstance(resultado, tuple):
                pila.extend(resultado)
                G.add_edge(argumentos[-1], resultado[-1])

# Crea un grafo de ejemplo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': [],
    'S': ['C'],
    'H': ['C']
}

# Define el nodo inicial y el nodo objetivo
nodo_inicial = 'D'
nodo_objetivo = 'G'

# Define la disposición de los nodos en la gráfica
pos = {
    'A': (0, 0),
    'B': (1, 0),
    'C': (1, 1),
    'D': (2, 0),
    'E': (2, 1),
    'F': (2, 2),
    'G': (3, 2),
    'S': (0, 1),
    'H': (2, 3)
}

# Crea el gráfico a partir del grafo
G = nx.Graph(grafo)
nx.draw(G, pos=pos, with_labels=True, font_weight='bold')
plt.show()

# Ejecuta el algoritmo HTN para explorar el grafo
plan = (explorar_grafo, grafo, nodo_inicial, nodo_objetivo)
ejecutar_tarea(plan, G)