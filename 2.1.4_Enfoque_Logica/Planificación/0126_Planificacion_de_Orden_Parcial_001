from collections import defaultdict

def partial_order_planning(actions, goals):
    plan = []
    causal_links = defaultdict(list)

    while goals:
        selected_action = None

        # Buscar una acción que cumpla todas las precondiciones y los enlaces causales
        for action in actions:
            if all(link in plan for link in causal_links[action]):
                selected_action = action
                break

        if selected_action is None:
            return None  # No se pudo encontrar un plan válido

        plan.append(selected_action)

        goals_copy = goals.copy()  # Crear una copia del conjunto de objetivos
        for goal in goals_copy:
            # Verificar si el objetivo está en los efectos de la acción seleccionada
            if goal in selected_action.effects:
                goals.remove(goal)
                # Agregar enlaces causales entre las precondiciones y la acción seleccionada
                for precond in selected_action.preconditions:
                    causal_links[precond].append(selected_action)

    return plan

# Definición de las acciones
class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

# Definición de los objetivos
goals = set(['A', 'B'])

# Definición de las acciones disponibles
actions = [
    Action('Action1', [], ['A']),
    Action('Action2', ['A'], ['B']),
    Action('Action3', [], ['B']),
]

# Ejecutar la planificación de orden parcial
plan = partial_order_planning(actions, goals)

# Mostrar el plan resultante
if plan is None:
    print('No se pudo encontrar un plan válido')
else:
    print('Plan encontrado:')
    for action in plan:
        print(action.name)

