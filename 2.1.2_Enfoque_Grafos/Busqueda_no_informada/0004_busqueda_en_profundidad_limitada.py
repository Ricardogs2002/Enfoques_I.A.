#Busqueda en profunfidad limitada
def busqueda_en_profundidad_limitada(problema, limite):
    resultado = None

    def buscar(nodo, profundidad):
        # Hacemos la variable resultado no local para que sea visible dentro de la función buscar()
        nonlocal resultado
        # Si el estado actual del nodo es el estado objetivo, retornamos el resultado
        if problema.es_estado_objetivo(nodo.estado):
            resultado = ([nodo.estado], True)
            return True
        # Si se alcanzó el límite de profundidad, retornamos False
        elif profundidad == limite:
            return False
        else:
            nodo_hijo_encontrado = False
            # Recorremos las acciones aplicables al estado actual del nodo
            for accion in problema.acciones_aplicables(nodo.estado):
                # Expandimos el nodo con la acción actual y creamos un hijo
                hijo = nodo.expandir(accion, problema)
                # Llamamos recursivamente a buscar() con el hijo y la profundidad incrementada
                if buscar(hijo, profundidad + 1):
                    # Si encontramos un nodo hijo que lleve a la solución, actualizamos la variable resultado
                    nodo_hijo_encontrado = True
                    resultado[0].insert(0, nodo.estado)
                    break
            return nodo_hijo_encontrado

    # Llamamos a buscar() con el nodo inicial y la profundidad inicial (0)
    buscar(problema.nodo_inicial(), 0)
    # Retornamos el resultado si se encontró, o (False, []) si no se encontró
    if resultado is not None:
        return resultado
    else:
        return (False, [])

    
""" 
El algoritmo de búsqueda en profundidad limitada solo seguirá buscando en una ruta 
particular hasta un cierto nivel de profundidad antes de retroceder y probar otra ruta.
Esta limitación se impone para evitar que el algoritmo se atasque en ramas de búsqueda 
inútiles y mejora la eficiencia de la búsqueda.
 Realiza una búsqueda en profundidad limitada en un problema dado hasta un límite dado.

Args:
problema: objeto de clase Problema que define el problema a resolver.
limite: límite de profundidad para la búsqueda en profundidad limitada.

Returns:
Una tupla que contiene un booleano y una lista:
- Un booleano que indica si se encontró la solución.
- Una lista con la secuencia de acciones que llevan a la solución (si se encontró).
"""
