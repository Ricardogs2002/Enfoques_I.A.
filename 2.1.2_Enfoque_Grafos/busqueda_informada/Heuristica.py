#Carlos Andres Riveramelo Del Toro
#Heuristica

#La heuristica es una estrategia que se utiliza paratomar decisiones en
#situaciones donde no hay una solucion optima, este programa nos da un
#ejemplo resolviendo un laberinto encontrando mediante algoritmos el ca-
#mino mas corto desde el inicio hasta el finaldel mismo.

#Posicion en el laberinto
class Nodo:
    def __init__(self, posicion, meta):
        self.posicion = posicion
        self.distancia = self.calcular_distancia(meta)

    def calcular_distancia(self, meta):
        x1, y1 = self.posicion
        x2, y2 = meta
        return abs(x1 - x2) + abs(y1 - y2)

#Encuentra el camino mas corto
def encontrar_camino(inicio, meta, laberinto):
    frontera = [Nodo(inicio, meta)]
    visitados = set()

    while frontera:
        #Seleccionar el nodo con la distancia heurística más baja
        nodo_actual = min(frontera, key=lambda nodo: nodo.distancia)
        frontera.remove(nodo_actual)

        #Verificar si se alcanzó la meta
        if nodo_actual.posicion == meta:
            return nodo_actual.posicion

        #Marcar el nodo como visitado
        visitados.add(nodo_actual.posicion)

        #Generar sucesores y agregarlos a la frontera
        x, y = nodo_actual.posicion
        sucesores = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        for sucesor in sucesores:
            if sucesor in visitados or sucesor not in laberinto:
                continue
            frontera.append(Nodo(sucesor, meta))

    return None

inicio = (0, 0)
meta = (4, 4)
laberinto = set([(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)])

camino = encontrar_camino(inicio, meta, laberinto)
if camino:
    print("Saliste del laberinto we :D", camino)
else:
    print("Te perdiste y te comio un minotauro :(")