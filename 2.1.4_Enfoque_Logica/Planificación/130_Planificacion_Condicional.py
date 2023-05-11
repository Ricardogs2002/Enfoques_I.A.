# Definimos una función para la planificación condicional
def planificacion_condicional(tarea):
    # Verificamos el tipo y la condición de la tarea utilizando estructuras de control condicional
    if tarea['tipo'] == 'tarea_1' and tarea['condicion'] is True:
        accion_1()  # Ejecutamos Acción 1 si se cumplen las condiciones
    elif tarea['tipo'] == 'tarea_2' and tarea['condicion'] is False:
        accion_2()  # Ejecutamos Acción 2 si se cumplen las condiciones
    elif tarea['tipo'] == 'tarea_3':
        accion_3()  # Ejecutamos Acción 3 si se cumple la condición del tipo de tarea
    else:
        print("No se encontró una regla correspondiente para la tarea.")  # Manejamos casos no definidos


# Definimos las acciones que se realizarán en cada caso
def accion_1():
    print("Realizando Acción 1")


def accion_2():
    print("Realizando Acción 2")


def accion_3():
    print("Realizando Acción 3")


# Ejemplo de uso:

# Creamos una tarea con tipo 'tarea_1' y condición True
tarea_1 = {'tipo': 'tarea_1', 'condicion': True}
planificacion_condicional(tarea_1)  # Se ejecutará Acción 1

# Creamos una tarea con tipo 'tarea_2' y condición False
tarea_2 = {'tipo': 'tarea_2', 'condicion': False}
planificacion_condicional(tarea_2)  # Se ejecutará Acción 2

# Creamos una tarea con tipo 'tarea_3' sin una condición específica
tarea_3 = {'tipo': 'tarea_3'}
planificacion_condicional(tarea_3)  # Se ejecutará Acción 3

# Creamos una tarea con tipo 'tarea_4' que no está definida en las reglas
tarea_4 = {'tipo': 'tarea_4', 'condicion': True}
planificacion_condicional(tarea_4)  # No se encontró una regla correspondiente
