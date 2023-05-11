"""En inteligencia artificial, una lista de decisiones se refiere a una
estructura de datos que se utiliza para representar y almacenar información
acerca de un conjunto de decisiones que se deben tomar en función de una serie
de condiciones o circunstancias específicas.

Por lo general, una lista de decisiones está compuesta por una serie de reglas,
cada una de las cuales especifica una condición y una acción asociada que se
debe tomar si se cumple la condición. Estas reglas suelen estar organizadas
en una estructura jerárquica que permite la evaluación de las condiciones y la
selección de la acción correspondiente."""



# Definir las variables de entrada
nota = float(input("Ingrese la nota del estudiante: ")) # Solicitar al usuario la nota del estudiante y convertirla a un número decimal
asistencia = float(input("Ingrese la asistencia del estudiante (%): ")) # Solicitar al usuario la asistencia del estudiante y convertirla a un número decimal

# Definir la lista de decisiones
decisiones = [
    {'condicion': nota >= 4.0 and asistencia >= 85, 'resultado': 'Aprobado'}, # Si la nota es mayor o igual a 4.0 y la asistencia es mayor o igual al 85%, el estudiante está aprobado
    {'condicion': nota >= 3.0 and asistencia >= 75, 'resultado': 'Regular'}, # Si la nota es mayor o igual a 3.0 y la asistencia es mayor o igual al 75%, el estudiante está regular
    {'condicion': nota < 3.0 or asistencia < 75, 'resultado': 'Reprobado'} # Si la nota es menor a 3.0 o la asistencia es menor al 75%, el estudiante está reprobado
]

# Evaluar las condiciones y determinar la calificación final
for decision in decisiones:
    if decision['condicion']: # Si la condición de la decisión es verdadera
        print("La calificación final del estudiante es:", decision['resultado']) # Mostrar el resultado asociado a la decisión
        break # Salir del bucle
