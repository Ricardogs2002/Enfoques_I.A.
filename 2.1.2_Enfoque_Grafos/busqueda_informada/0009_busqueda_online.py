

from queue import Queue

def resolver_laberinto(mapa, inicio):
    visitados = set()  # Conjunto de nodos visitados
    cola = Queue()  # Cola para almacenar los nodos por visitar
    cola.put(inicio)

    while not cola.empty():
        actual = cola.get()
        fila, col = actual

        # Si hemos llegado al objetivo, hemos resuelto el laberinto
        if mapa[fila][col] == 2:
            return True

        # Si el nodo actual no ha sido visitado, lo añadimos al conjunto de visitados
        if actual not in visitados:
            visitados.add(actual)

            # Añadimos a la cola los vecinos que no son paredes y que no han sido visitados
            for df, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nf, nc = fila + df, col + dc
                if 0 <= nf < len(mapa) and 0 <= nc < len(mapa[0]) and mapa[nf][nc] != 1 and (nf, nc) not in visitados:
                    cola.put((nf, nc))

    # Si llegamos aquí, no hemos encontrado la salida del laberinto
    return False

# Ejemplo de uso
mapa = [[0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 2, 0]]

inicio = (0, 0)
if resolver_laberinto(mapa, inicio):
    print("¡Se ha encontrado la salida del laberinto!")
else:
    print("No se ha encontrado la salida del laberinto.")
