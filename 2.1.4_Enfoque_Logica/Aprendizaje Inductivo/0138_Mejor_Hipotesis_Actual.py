#Mejor hipotesis
"""
La mejor hipótesis (en inglés, Best Hypothesis) es un concepto
que se utiliza en diversas áreas de la programación y la 
inteligencia artificial. Se refiere a la hipótesis que mejor 
explica los datos disponibles en un momento determinado. En otras
palabras, se trata de la hipótesis que, en un determinado momento,
es la más probable de ser verdadera, dado el conocimiento y los
datos disponibles.

La mejor hipótesis es un concepto útil en programación porque 
permite simplificar el proceso de toma de decisiones en situaciones
en las que hay múltiples posibilidades y hay que escoger la que 
tiene mayor probabilidad de ser verdadera. En muchos casos, las 
hipótesis son complejas y hay muchos datos a tener en cuenta, 
por lo que tener una manera de identificar rápidamente la hipótesis
más probable puede ahorrar tiempo y recursos.
"""

import hypothesis.strategies as st  # Importar el módulo "strategies" de la biblioteca "Hypothesis" y asignarle el alias "st"
from hypothesis import given  # Importar la función "given" de la biblioteca "Hypothesis"

# Decorar la función "test_addition_is_commutative" con el generador de estrategias "given"
@given(st.integers(), st.integers())
def test_addition_is_commutative(x, y):  # Definir la función "test_addition_is_commutative" que toma dos argumentos
    assert x + y >= x  # Asegurarse de que la suma de "x" y "y" es mayor o igual que "x"
    assert x + y >= y  # Asegurarse de que la suma de "x" y "y" es mayor o igual que "y"

#La biblioteca hypothesis nos proporciona herramientas para generar datos de prueba
#de manera automatica. Util para la generacion de pruebas de sofware.Si una propiedad 
#de prueba falla, la biblioteca intentará reducir el caso de prueba a un ejemplo mínimo 
#y proporcionará información sobre el fallo
#la función test_addition_is_commutative(x, y):prueba si la suma es conmutativa, lo que significa que cambiar el orden de 
#los operandos no cambia el resultado. Si la prueba falla, significa que la propiedad conmutativa de la suma se viola para 
#algunos valores de entrada
#@given(st.integers(), st.integers()) especifica que los argumentos para la función test_addition_is_commutative() serán generados 
#aleatoriamente por las estrategias st.integers(), que generan números enteros aleatorios
#La función decorada se ejecutará múltiples veces, cada vez con diferentes datos de entrada generados por las estrategias especificadas. 
#Al hacerlo, se pueden detectar errores en el código que no se habrían encontrado con pruebas manuales, y se puede verificar que la función 
#funciona correctamente para diferentes valores de entrada.
#assert es una instrucción en Python que se utiliza para verificar que una expresión sea verdadera. Si la expresión es falsa, assert lanzará una 
#excepción AssertionError y el programa se detendrá
#







