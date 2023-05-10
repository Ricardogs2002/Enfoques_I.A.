import pulp

# Crear el problema
prob = pulp.LpProblem("Ejemplo", pulp.LpMinimize)

# Definir variables
x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous') # Variable de decisión x1
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous') # Variable de decisión x2

# Definir función objetivo
prob += 4*x1 + 5*x2 # Función objetivo a minimizar: 4x1 + 5x2

# Definir restricciones
prob += 3*x1 + 4*x2 >= 1 # Restricción 1: 3x1 + 4x2 >= 1
prob += 2*x1 + 1*x2 >= 2 # Restricción 2: 2x1 + x2 >= 2

# Resolver el problema
prob.solve()

# Imprimir el resultado
print("Estado:", pulp.LpStatus[prob.status]) # Imprimir el estado de la solución (óptimo, no factible, etc.)
print("Valor óptimo:", pulp.value(prob.objective)) # Imprimir el valor óptimo de la función objetivo
print("Solución:") # Imprimir la solución (valores de las variables de decisión)
for v in prob.variables():
    print(v.name, "=", pulp.value(v)) # Imprimir el nombre y el valor de cada variable de decisión


"""
La planificación continua y multiagente es un enfoque 
clave en el campo de la inteligencia artificial (IA) y se utiliza
en una variedad de aplicaciones de IA, como en la robótica, la 
automatización de procesos, los sistemas de transporte inteligente, la logística y la gestión de recursos.
En la robótica, por ejemplo, la planificación continua y 
multiagente permite que los robots trabajen juntos de manera 
coordinada para realizar tareas complejas y adaptarse a cambios 
en el entorno. Los robots pueden comunicarse entre sí para compartir 
información y ajustar sus planes a medida que cambian las circunstancias.
"""
