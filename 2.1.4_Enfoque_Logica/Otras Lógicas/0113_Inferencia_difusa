# Implementación de inferencia difusa con ejemplo de control de temperatura

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Importar las librerías necesarias

# Crear variables de entrada y salida difusa
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'ventilador')

# Crear variables difusas de entrada y salida, con universos de discurso de 0 a 100,
# y nombres 'temperatura' y 'ventilador' respectivamente.

# Definir funciones de membresía difusa
temperatura['fría'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['templada'] = fuzz.trimf(temperatura.universe, [0, 50, 100])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

ventilador['bajo'] = fuzz.trimf(ventilador.universe, [0, 0, 50])
ventilador['medio'] = fuzz.trimf(ventilador.universe, [0, 50, 100])
ventilador['alto'] = fuzz.trimf(ventilador.universe, [50, 100, 100])

# Definir las funciones de membresía difusa de cada variable de entrada y salida.
# Se utilizan funciones de pertenencia triangular para cada una, que se definen mediante
# los parámetros que representan los puntos donde la función cambia de valor.

# Definir reglas difusas
regla1 = ctrl.Rule(temperatura['fría'], ventilador['bajo'])
regla2 = ctrl.Rule(temperatura['templada'], ventilador['medio'])
regla3 = ctrl.Rule(temperatura['caliente'], ventilador['alto'])

# Definir las reglas difusas que relacionan la temperatura con el nivel del ventilador.
# En cada regla se establece qué función de pertenencia de la temperatura se utiliza para
# evaluar la regla, y qué función de pertenencia del nivel del ventilador se obtiene como
# resultado.

# Crear sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
sistema = ctrl.ControlSystemSimulation(sistema_control)

# Crear el sistema de control difuso, que incluye las reglas difusas definidas previamente.

# Asignar valores de entrada al sistema
sistema.input['temperatura'] = 75

# Asignar el valor de entrada deseado al sistema, en este caso se establece que la
# temperatura es de 75 grados.

# Obtener valor de salida difusa
sistema.compute()

# Obtener el valor difuso resultante del sistema, utilizando el valor de entrada
# establecido anteriormente.

# Imprimir valor de salida
print(sistema.output['ventilador'])

# Imprimir en la consola el valor de salida difuso obtenido, en este caso el
# nivel del ventilador correspondiente a una temperatura de 75 grados.
