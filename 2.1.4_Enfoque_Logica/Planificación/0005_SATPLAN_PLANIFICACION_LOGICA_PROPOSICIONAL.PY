# -*- coding: utf-8 -*-
"""
Created on Fri May 12 18:16:56 2023

@author: 52331
"""

# Importamos la librería Pycosat, que es una implementación en Python del algoritmo de satisfacibilidad Booleana (SAT)
import pycosat

# Definimos la función principal de SATPLAN
def satplan(initial_state, goal_state, actions, literals):

    # Inicializamos el plan como una lista vacía
    plan = []

    # Iteramos hasta encontrar un plan válido o hasta que no queden más iteraciones
    while True:

        # Definimos las variables proposicionales como un conjunto que contiene los estados iniciales y los objetivos
        props = set(initial_state) | set(goal_state)

        # Añadimos las precondiciones y efectos de todas las acciones como cláusulas
        clauses = []

        for action in actions:
            # La precondición de una acción es una cláusula que contiene la negación de sus condiciones negadas
            precond = [-lit for lit in action.precond]  # Negamos las condiciones
            precond.append(action.effect)  # Añadimos el efecto
            clauses.append(precond)

        # Añadimos las cláusulas que expresan que un literal no puede ser verdadero y falso al mismo tiempo
        for literal in literals:
            clauses.append([literal, -literal])

        # Añadimos las cláusulas que representan los estados iniciales y los objetivos
        for state in initial_state:
            clauses.append([state])
        for state in goal_state:
            clauses.append([state])

        # Llamamos al algoritmo de satisfacibilidad Booleana con las cláusulas definidas
        result = pycosat.solve(clauses)

        # Si no se encontró una solución, devolvemos None
        if result == "UNSAT":
            return None

        # Si se encontró una solución, construimos el plan a partir de las variables proposicionales que son verdaderas en la solución
        plan = []
        for prop in props:
            if prop in result:
                # Si el literal es verdadero, añadimos la acción correspondiente al plan
                if isinstance(prop, tuple) and prop[0] == "action":
                    plan.append(prop[1])
        return plan
#Este programa utiliza la librería Pycosat para implementar el algoritmo de 
#satisfacibilidad Booleana. La función satplan toma como entrada el estado inicial, 
#el estado objetivo, las acciones disponibles y los literales que se pueden utilizar. 
#El programa se ejecuta en un bucle que se repite hasta que se encuentra un plan 
#válido o hasta que no quedan más iteraciones. En cada iteración, se construyen
# las cláusulas que representan las precondiciones y efectos de todas las acciones,
# así como las cláusulas que representan los estados iniciales y objetivos. Luego se
# llama al algoritmo de satisfacibilidad Booleana con estas cláusulas para determinar
# si existe una solución. Si se encuentra una solución, se construye el plan a partir
# de las variables proposicionales que son verdaderas en la solución. Si no se 
# encuentra una solución, se devuelve None.
