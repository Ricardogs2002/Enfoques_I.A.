"""
Dentro del enfoque de la lógica en la inteligencia artificial, la incertidumbre y los factores de certeza se 
refieren a la capacidad de un sistema de inteligencia artificial para manejar información incompleta o 
ambigua, y para asignar grados de certeza o probabilidad a diferentes proposiciones.

La incertidumbre se refiere a la falta de información completa sobre un estado o evento. En el contexto 
de la inteligencia artificial, esto puede incluir datos incompletos o inconsistentes, o una falta de 
conocimiento sobre cómo se relacionan diferentes variables.

Los factores de certeza se refieren a la capacidad de un sistema de inteligencia artificial para manejar 
diferentes grados de certeza o probabilidad asociados con diferentes proposiciones. Por ejemplo, un sistema 
de inteligencia artificial puede ser capaz de decir que "hay una alta probabilidad de que llueva mañana" 
o "hay una baja probabilidad de que llueva mañana".

La gestión de la incertidumbre y los factores de certeza es un área importante de investigación en la 
inteligencia artificial, ya que permite a los sistemas de IA tomar decisiones más informadas en situaciones 
donde la información es incompleta o ambigua
"""
import random

# Simulación del lanzamiento de una moneda
def flip_coin():
    return random.randint(0, 1)

# Generar una lista de resultados de lanzamientos
results = [flip_coin() for _ in range(100)]

# Contar el número de veces que se obtiene cara
num_heads = sum(results)
num_tails = len(results) - num_heads

# Estimación de la probabilidad de obtener cara
p = num_heads / len(results)

# Análisis de los resultados
print("Número de veces que se obtiene cara:", num_heads)
print("Número de veces que se obtiene cruz:", num_tails)
print("Probabilidad de obtener cara:", p)


"""


En este ejemplo, se utiliza la simulación del lanzamiento de una moneda para generar una lista de resultados. 
Luego, se cuenta el número de veces que se obtiene cara y se utiliza este número para estimar la probabilidad 
de obtener cara.

La incertidumbre se refleja en la variabilidad de los resultados posibles y en la falta de certeza en la 
estimación de la probabilidad de obtener cara. Los factores de certeza se reflejan en la cantidad de veces 
que se obtiene cara en la muestra y en la precisión de la estimación de la probabilidad.

Este ejemplo ilustra cómo se puede utilizar la gestión de la incertidumbre y los factores de certeza en un 
contexto sencillo y cómo se pueden utilizar estadísticas básicas para analizar los resultados y estimar la 
probabilidad de un evento.
"""
