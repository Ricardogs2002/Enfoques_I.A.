import math


class Nodo:
    def __init__(self, valor, hijos=None):
        self.valor = valor
        self.hijos = hijos or []

    def __repr__(self):
        return f"Nodo({self.valor})"

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

# verificar si se alcanzó la profundidad máxima del árbol de juego o si el nodo actual no tiene hijos
def minimax(nodo, profundidad, maximizar):
    if profundidad == 0 or not nodo.hijos:
        return nodo.valor, None

    if maximizar:
        valor = -math.inf
        mejor_movimiento = None
        for hijo in nodo.hijos:
            valor_hijo, _ = minimax(hijo, profundidad - 1, False)
            if valor_hijo > valor:
                valor = valor_hijo
                mejor_movimiento = hijo
    else:
        valor = math.inf
        mejor_movimiento = None
        for hijo in nodo.hijos:
            valor_hijo, _ = minimax(hijo, profundidad - 1, True)
            if valor_hijo < valor:
                valor = valor_hijo
                mejor_movimiento = hijo

    return valor, mejor_movimiento


# Ejemplo de uso
nodo1 = Nodo(3)
nodo2 = Nodo(5)
nodo3 = Nodo(7)
nodo4 = Nodo(1)
nodo5 = Nodo(2)
nodo6 = Nodo(6)
nodo7 = Nodo(9)
nodo8 = Nodo(8)

nodo1.agregar_hijo(nodo2)
nodo1.agregar_hijo(nodo3)
nodo2.agregar_hijo(nodo4)
nodo2.agregar_hijo(nodo5)
nodo3.agregar_hijo(nodo6)
nodo3.agregar_hijo(nodo7)
nodo7.agregar_hijo(nodo8)

valor, movimiento = minimax(nodo1, profundidad=2, maximizar=True)
print(f"Mejor valor: {valor}")
print(f"Mejor movimiento: {movimiento}")

