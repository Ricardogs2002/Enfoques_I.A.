

import numpy as np
#Librería usada para lógica difusa
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Creación de variables de entrada y salida difusas
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
velocidad = ctrl.Antecedent(np.arange(0, 11, 1), 'velocidad')
"ctrl.Antecedent:Variable antecedente (entrada/sensor) para un sistema de control difuso."
#se crean dos variables de entrada difusas llamadas "temperatura" y "velocidad"
#Se especifica el rango de los valores posibles para cada variable utilizando np.arange()
#donde el primer argumento es el valor inicial, el segundo argumento es el valor final y 
#el tercer argumento es el paso. 

flujo = ctrl.Consequent(np.arange(0, 11, 1), 'flujo')
"ctrl.Consequent:Variable consecuente (salida/control) para un sistema de control difuso."
#Crea una variable de salida difusa. En el ejemplo, se crea una variable de salida 
#difusa llamada "flujo" utilizando el mismo enfoque que se utilizó 
#para las variables de entrada difusas.

# Definición de conjuntos difusos y funciones de membresía
"fuzz.trimf(x,abc):Triangular membership function generator."
#la función fuzz.trimf() se puede utilizar para generar una función de pertenencia triangular.
#Toma dos argumentos: una matriz que representa el universo de discurso para la variable
# y una lista de tres valores que representan el límite inferior, el punto medio y 
#el límite superior de la función triangular. La función devuelve una matriz del mismo
# tamaño que la matriz del universo, con los valores de la función de pertenencia en cada
# punto del universo.
temperatura['baja'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['media'] = fuzz.trimf(temperatura.universe, [25, 50, 75])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

velocidad['baja'] = fuzz.trimf(velocidad.universe, [0, 0, 5])
velocidad['alta'] = fuzz.trimf(velocidad.universe, [5, 10, 10])

flujo['bajo'] = fuzz.trimf(flujo.universe, [0, 0, 5])
flujo['medio'] = fuzz.trimf(flujo.universe, [2.5, 5, 7.5])
flujo['alto'] = fuzz.trimf(flujo.universe, [5, 10, 10])

# Definición de reglas difusas
regla1 = ctrl.Rule(temperatura['baja'] | velocidad['baja'], flujo['bajo'])
regla2 = ctrl.Rule(temperatura['media'] | velocidad['alta'], flujo['medio'])
regla3 = ctrl.Rule(temperatura['alta'] | velocidad['alta'], flujo['alto'])

# Creación del sistema de control difuso
sistema_ctrl = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

# Asignación de valores a las variables de entrada
sistema.input['temperatura'] = 70
sistema.input['velocidad'] = 3

# Evaluación del sistema difuso
sistema.compute()

# Obtención del resultado difuso
resultado = sistema.output['flujo']
print("Resultado:", resultado)

# Visualización de las funciones de membresía
temperatura.view()
velocidad.view()
flujo.view()
