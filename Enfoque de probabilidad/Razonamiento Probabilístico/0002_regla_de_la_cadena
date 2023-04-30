import networkx as nx

# Creamos un grafo dirigido y etiquetado
G = nx.DiGraph()
G.add_edge('Michoacan', 'Colima', weight=4.78)
G.add_edge('Michoacan', 'Guanajuato', weight=1.76)
G.add_edge('Colima', 'Jalisco', weight=1.92)
G.add_edge('Jalisco', 'Nayarit', weight=2.05)
G.add_edge('Jalisco', 'Guanajuato', weight=2.72)
G.add_edge('Nayarit', 'Sinaloa', weight=4.80)
G.add_edge('Nayarit', 'Zacatecas', weight=5.54)
G.add_edge('Sinaloa', 'Nuevo León', weight=10.41)
G.add_edge('Nuevo León', 'Querétaro', weight=7.08)
G.add_edge('Querétaro', 'Guanajuato', weight=1.48)
G.add_edge('Guanajuato', 'Zacatecas', weight=3.09)


def backward_propagation(G, objetivo):
    # Inicializar los valores de sensibilidad para todos los nodos en el grafo como cero.
    for node in G.nodes:
        G.nodes[node]['sensibilidad'] = 0.0
        
    # Establecer el valor de sensibilidad del nodo objetivo en 1.
    G.nodes[objetivo]['sensibilidad'] = 1.0
    
    # Propagar hacia atrás la sensibilidad desde el nodo objetivo hasta los nodos de entrada.
    for node in reversed(list(nx.topological_sort(G))):
        if node != objetivo:
            # Calcular el valor de sensibilidad para el nodo actual sumando las sensibilidades de los nodos sucesores.
            sensibilidad = sum([G.nodes[succ]['sensibilidad'] * G[node][succ]['weight'] for succ in G.successors(node)])
            
            # Actualizar el valor de sensibilidad para el nodo actual.
            G.nodes[node]['sensibilidad'] = sensibilidad

objetivo = 'Zacatecas'

backward_propagation(G, objetivo)

print(f"La sensibilidad del nodo 'Michoacan' es {G.nodes['Michoacan']['sensibilidad']}")

nx.draw(G, with_labels=True)
