

import networkx as nx
import matplotlib.pyplot as plt

# Lista de nodos del grafo; Nodo origen, destino y peso
G = [["A", "B", 20], ["A", "C", 7], ["B", "C", 15], ["B", "D", 15], ["C", "D", 25], ["C", "E", 6], ["D", "E", 4], ["C", "F", 7], ["F", "A", 6], ["F", "G", 4], ["G", "E", 20], ["G", "H", 6], ["H", "B", 12]]

# Crear grafo vacio
G_nx = nx.Graph()
# Añadimos los parametros de cada nodo de la lista
for Origen, Destino, Peso in G:
    G_nx.add_edge(Origen, Destino, weight=Peso)

#Arbol Parcial Minimo de Kruskal
Minima = nx.minimum_spanning_tree(G_nx)

# Arbol de expancion maxima
Maxima = nx.maximum_spanning_tree(G_nx)

# Visualizar el grafo Original
pos = nx.circular_layout(G_nx)

# Configurar la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar el árbol de expansión mínima
nx.draw_networkx(Minima, pos, with_labels=True, ax=ax, node_color='blue', edge_color='blue', width=2)

# Dibujar el árbol de expansión máxima
nx.draw_networkx(Maxima, pos, with_labels=True, ax=ax, node_color='red', edge_color='red', width=2)

# Mostrar los pesos de los bordes
labels = nx.get_edge_attributes(G_nx, 'weight')
nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=labels, ax=ax)

# Configurar el título y mostrar la figura
ax.set_title("Árbol de expansión mínima (azul) y máxima (rojo)")
plt.show()
