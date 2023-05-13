
#Poda Alfa-Beta

#La poda alfa-beta se utiliza para mejorar la eficiencia de los algoritmos
#en juegos de adversarios donde debes de encontrar la mejor jugada como el
#ajedres o el gato, juegos de competencia, en este programa cree un conju-
#nto de nodos para encontrar el mejor valor

#Definir la estructura de un nodo en el árbol
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

#Función de poda alfa-beta
def poda_alfa_beta(nodo, alfa, beta, esMaximizador):
    if esMaximizador:
        for hijo in nodo.hijos:
            alfa = max(alfa, poda_alfa_beta(hijo, alfa, beta, False))
            if beta <= alfa:
                break  #Poda beta
        return alfa
    else:
        for hijo in nodo.hijos:
            beta = min(beta, poda_alfa_beta(hijo, alfa, beta, True))
            if beta <= alfa:
                break  #Poda alfa
        return beta

#Construir el árbol de búsqueda
raiz = Nodo(0)
nodo1 = Nodo(5)
nodo2 = Nodo(3)
nodo3 = Nodo(6)
nodo4 = Nodo(2)
nodo5 = Nodo(1)

raiz.agregar_hijo(nodo1)
raiz.agregar_hijo(nodo2)
nodo1.agregar_hijo(nodo3)
nodo1.agregar_hijo(nodo4)
nodo2.agregar_hijo(nodo5)

#Ejecutar la poda alfa-beta en el árbol
mejor_valor = poda_alfa_beta(raiz, float('-inf'), float('inf'), True)

print("Mejor valor encontrado:", mejor_valor)
