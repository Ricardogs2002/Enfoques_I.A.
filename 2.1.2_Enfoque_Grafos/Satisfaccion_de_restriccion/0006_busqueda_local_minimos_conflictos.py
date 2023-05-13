#Busqueda local de minimos conflictos
import random

def busqueda_local_min_conflictos(problema, max_iter=1000, max_pasos=100):

    # Generar estado inicial aleatorio
    estado_actual = problema.estado_aleatorio()

    for i in range(max_iter):
        # Comprobar si el estado actual es objetivo
        if problema.es_estado_objetivo(estado_actual):
            return ([estado_actual], True)

        # Realizar búsqueda local de mínimos conflictos
        for j in range(max_pasos):
            # Obtener la lista de variables conflictivas en el estado actual
            var_conflictivas = problema.variables_conflictivas(estado_actual)

            # Comprobar si no hay variables conflictivas
            if not var_conflictivas:
                break

            # Escoger una variable conflictiva aleatoria
            var = random.choice(var_conflictivas)

            # Escoger un valor para la variable conflictiva que minimice los conflictos
            val = problema.valor_min_conflictos(var, estado_actual)

            # Asignar el valor a la variable
            estado_actual[var] = val

    # Si no se encontró solución, retornar False y una lista vacía
    return (False, [])

"""
La búsqueda local de mínimos conflictos consiste en encontrar
las variables conflictivas en el estado actual, escoger una 
variable conflictiva aleatoria y asignarle un valor que minimice 
los conflictos. Este proceso se repite hasta que se llegue a
un estado en el que no haya variables conflictivas o se 
alcance el número máximo de pasos permitidos.

La función retorna una tupla con un booleano que indica si 
se encontró la solución y una lista con la secuencia de acciones
que llevan a dicha solución.
Realiza una búsqueda local de mínimos conflictos para resolver
un problema.

Args:
problema: objeto de clase Problema que define el problema a resolver.
max_iter: número máximo de iteraciones permitidas.
max_pasos: número máximo de pasos permitidos en cada iteración.

Returns:
Una tupla que contiene un booleano y una lista:
- Un booleano que indica si se encontró la solución.
- Una lista con la secuencia de acciones que llevan a la solución 
(si se encontró).
"""
