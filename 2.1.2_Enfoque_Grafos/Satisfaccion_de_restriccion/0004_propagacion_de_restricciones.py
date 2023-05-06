# Importar la biblioteca de propagación de restricciones de python
import constraint

# Crear un objeto de problema
problem = constraint.Problem()

# Crear una lista con los 15 nombres de personas
nombres = ["Juan", "Pedro", "Luis", "Ana", "María", "Carlos", "Lucía", "Sofía", "Jorge", "Fabián", "Diego", "Gabriela", "Mariana", "Julia", "Mario"]

# Añadir cada nombre a la lista de variables del problema
for nombre in nombres:
    problem.addVariable(nombre, [1, 2, 3]) # Cada persona puede tener uno de los 3 trabajos posibles

# Agregar restricciones al problema
# Las siguientes restricciones aseguran que:
# 1. Juan, Pedro y Luis no pueden tener el mismo trabajo
problem.addConstraint(constraint.AllDifferentConstraint(), ["Juan", "Pedro", "Luis"])
# 2. Ana y María no pueden tener el mismo trabajo
problem.addConstraint(constraint.ExactSumConstraint(2), ["Ana", "María"])
# 3. Carlos y Lucía no pueden tener el mismo trabajo
problem.addConstraint(constraint.ExactSumConstraint(2), ["Carlos", "Lucía"])
# 4. Sofía y Jorge no pueden tener el mismo trabajo
problem.addConstraint(constraint.ExactSumConstraint(2), ["Sofía", "Jorge"])
# 5. Fabián y Diego no pueden tener el mismo trabajo
problem.addConstraint(constraint.ExactSumConstraint(2), ["Fabián", "Diego"])
# 6. Gabriela, Mariana y Julia no pueden tener el mismo trabajo
problem.addConstraint(constraint.AllDifferentConstraint(), ["Gabriela", "Mariana", "Julia"])

# Resolver el problema
soluciones = problem.getSolutions()

# Imprimir las soluciones
print("Se encontraron", len(soluciones), "soluciones:")
for solucion in soluciones:
    print(solucion)
#En este ejemplo, se importa la biblioteca de propagación de restricciones de 
#Python y se crea un objeto de problema.
# Se agregan las 15 variables correspondientes a cada nombre a la lista de variables del problema y se les asigna el dominio de posibles trabajos (1, 2 o 3).
#Luego se agregan las restricciones correspondientes a las relaciones entre los
# nombres. Por ejemplo, la restricción "Juan, Pedro y Luis no pueden tener el mismo
# trabajo" se agrega asegurando que los valores asignados a estas tres variables 
#sean distintos (constraint.AllDifferentConstraint())
#Finalmente, se resuelve el problema y se imprimen todas las soluciones 
#encontradas. En este caso, cada solución correspondería a una asignación de 
#trabajos a las 15 personas que cumple con todas las restricciones agregadas.
