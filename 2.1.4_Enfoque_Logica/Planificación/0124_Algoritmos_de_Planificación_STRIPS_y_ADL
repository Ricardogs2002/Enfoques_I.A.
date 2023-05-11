# Areli Sarai García Medina | 20310380
# Algoritmo STRIPS

# Definimos un diccionario con las tareas y sus precondiciones
tareas = {
    'Hacer la cama': {'Cama desordenada': True},
    'Cocinar el desayuno': {'Cocina limpia': True, 'Ingredientes disponibles': True},
    'Llevar al perro a pasear': {'Perro esperando': True, 'Correa disponible': True},
    'Hacer la compra': {'Lista de la compra preparada': True},
    'Lavar la ropa': {'Ropa sucia acumulada': True, 'Detergente disponible': True}
}

# Definimos una función que verifica si una tarea se puede realizar
def tarea_realizable(tarea, estado):
    for precondicion, valor in tareas[tarea].items():
        if valor != estado[precondicion]:
            return False
    return True

# Definimos la función principal que organiza las tareas
def organizar_tareas(estado_inicial):
    # Creamos una lista con todas las tareas pendientes
    tareas_pendientes = list(tareas.keys())
    # Establecemos el estado actual como el estado inicial
    estado_actual = estado_inicial
    # Creamos una lista vacía para almacenar las acciones realizadas
    acciones_realizadas = []

    # Mientras haya tareas pendientes
    while tareas_pendientes:
        # Buscamos la primera tarea pendiente que se pueda realizar
        tarea_actual = None
        for tarea in tareas_pendientes:
            if tarea_realizable(tarea, estado_actual):
                tarea_actual = tarea
                break

        # Si no se puede realizar ninguna tarea, terminamos la función
        if tarea_actual is None:
            print('No se pueden realizar más tareas')
            return acciones_realizadas

        # Imprimimos la tarea que se va a realizar
        print(f'Realizando tarea: {tarea_actual}')
        # Eliminamos la tarea pendiente de la lista de tareas pendientes
        tareas_pendientes.remove(tarea_actual)
        # Añadimos la tarea realizada a la lista de acciones realizadas
        acciones_realizadas.append(tarea_actual)

        # Actualizamos el estado actual con los efectos de la tarea realizada
        for efecto, valor in tareas[tarea_actual].items():
            estado_actual[efecto] = valor

    # Si se han realizado todas las tareas, devolvemos la lista de acciones realizadas
    return acciones_realizadas

# Creamos un estado inicial con todas las condiciones en False
estado_inicial = {
    'Cama desordenada': True,
    'Cocina limpia': False,
    'Ingredientes disponibles': True,
    'Perro esperando': False,
    'Correa disponible': True,
    'Lista de la compra preparada': False,
    'Ropa sucia acumulada': True,
    'Detergente disponible': True
}

# Llamamos a la función principal para organizar las tareas
acciones_realizadas = organizar_tareas(estado_inicial)

# Imprimimos la lista de acciones realizadas
print('Acciones realizadas:')
for accion in acciones_realizadas:
    print(f'- {accion}')
