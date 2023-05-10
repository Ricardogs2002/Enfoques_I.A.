def es_solucion(solucion_actual, espacio_solucion):
    """
    Función que comprueba si la solución actual es una solución completa.
    En este ejemplo, una solución completa es una permutación de todos los elementos del espacio de solución.
    """
    return set(solucion_actual) == set(espacio_solucion)

def es_valido(candidato):
    """
    Función que comprueba si un candidato es válido.
    En este ejemplo, todos los candidatos son válidos.
    """
    return True

def generar_candidatos(espacio_solucion, solucion_actual):
    """
    Función que genera una lista con todos los posibles candidatos a añadir a la solución actual.
    En este ejemplo, los candidatos son todos los elementos del espacio de solución que no están en la solución actual.
    """
    return [x for x in espacio_solucion if x not in solucion_actual]

def backtracking(espacio_solucion, solucion_actual):
    """
    Función que implementa el algoritmo de backtracking.
    Devuelve una lista con todas las soluciones encontradas.
    """
    soluciones = []
    # Si hemos encontrado una solución, la añadimos a la lista de soluciones.
    if es_solucion(solucion_actual, espacio_solucion):
        soluciones.append(solucion_actual.copy())  # Copiamos la solución actual para que no se modifique en las iteraciones siguientes.
    # Si no hemos encontrado una solución, continuamos buscando.
    else:
        # Generamos todas las posibles soluciones candidatas a partir de la solución actual.
        candidatos = generar_candidatos(espacio_solucion, solucion_actual)
        # Para cada candidato, comprobamos si es una solución válida y seguimos explorando.
        for candidato in candidatos:
            if es_valido(candidato):
                # Añadimos el candidato a la solución actual.
                solucion_actual.append(candidato)
                # Llamamos recursivamente a la función con la solución actualizada y concatenamos las soluciones encontradas.
                soluciones += backtracking(espacio_solucion, solucion_actual)
                # Una vez que hemos terminado de explorar esta rama, eliminamos el último elemento de la solución actual.
                solucion_actual.pop()
    # Devolvemos la lista de soluciones encontradas.
    return soluciones

# Ejemplo de uso de la función backtracking
espacio_solucion = [1, 2, 3]
solucion_inicial = []
soluciones_encontradas = backtracking(espacio_solucion, solucion_inicial)
print("Soluciones encontradas:")
for solucion in soluciones_encontradas:
    print(solucion)

    """
    La idea principal detrás del backtracking es explorar 
    todas las posibles soluciones de un problema en un árbol de 
    búsqueda, descartando aquellas que no cumplen ciertas 
    restricciones o condiciones (poda de ramas), hasta encontrar 
    la solución deseada. Si en algún momento se llega a un punto
     en el que no es posible avanzar más sin violar alguna restricción, 
     se retrocede (backtrack) a la última decisión tomada 
     y se prueba con otra alternativa.
    """
