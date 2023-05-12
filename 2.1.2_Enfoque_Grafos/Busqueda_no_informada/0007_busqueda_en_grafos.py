# Definición de la clase Grafo
class Grafo:
    def __init__(self):
        self.grafo = {}

    # Función para agregar una arista al grafo
    def agregar_arista(self, u, v):
        if u in self.grafo:
            self.grafo[u].append(v)
        else:
            self.grafo[u] = [v]

    # Función de búsqueda en profundidad (DFS)
    def dfs(self, nodo):
        # Lista para rastrear los nodos visitados
        visitados = []

        # Llamada a la función auxiliar para realizar la búsqueda en profundidad
        self._dfs_util(nodo, visitados)

    # Función auxiliar para la búsqueda en profundidad
    def _dfs_util(self, nodo, visitados):
        # Marcar el nodo actual como visitado y agregarlo a la lista
        visitados.append(nodo)
        print(nodo, end=" ")

        # Recorrer los nodos adyacentes no visitados
        if nodo in self.grafo:
            for adyacente in self.grafo[nodo]:
                if adyacente not in visitados:
                    self._dfs_util(adyacente, visitados)


# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista(0, 1)
grafo.agregar_arista(0, 2)
grafo.agregar_arista(1, 2)
grafo.agregar_arista(2, 0)
grafo.agregar_arista(2, 3)
grafo.agregar_arista(3, 3)

print("Recorrido DFS (empezando desde el nodo 2):")
grafo.dfs(2)
