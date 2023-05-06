"""
La probabilidad a priori es un concepto fundamental en la teoría de la probabilidad 
y se refiere a la probabilidad de un evento antes de que se observen los datos o la evidencia. 
Es una estimación inicial de la probabilidad basada en la información previa disponible antes de la observación.

La probabilidad a priori puede cambiar si se dispone de nueva información o si se tienen nuevas hipótesis 
o suposiciones acerca del fenómeno en cuestión. En algunos casos, esta información nueva puede ser más precisa
o más confiable que la información previa, lo que llevaría a ajustar las probabilidades a priori.
También es posible que se modifique la probabilidad a priori si se considera que los eventos que la determinan 
han cambiado o si se dispone de una cantidad suficiente de datos para actualizar las estimaciones iniciales.


Un ejemplo en el que la probabilidad a priori cambia podría ser el siguiente:

Supongamos que deseas saber la probabilidad de que llueva en una ciudad en un día determinado. 
Si no tienes ninguna información adicional, tu probabilidad a priori de que llueva podría ser
 del 50% (ya que podría llover o no llover). Sin embargo, si consultas el pronóstico del tiempo 
 y observas que hay una baja presión atmosférica en la región, podrías actualizar tu probabilidad 
 a priori y aumentarla a, por ejemplo, el 70%, ya que la baja presión atmosférica aumenta la probabilidad de lluvia.

Ahora, si el día transcurre sin llover, podrías volver a actualizar tu probabilidad a priori y 
reducirla a, por ejemplo, el 30%, ya que la falta de lluvia indica que las condiciones atmosféricas no 
eran lo suficientemente favorables para la lluvia.
"""


import numpy as np

# Generamos una lista de 100 números aleatorios del 1 al 10
numeros = np.random.randint(1, 11, 100)

# Suponemos que la probabilidad a priori de que un número sea mayor que 5 es 0.4
prob_priori_mayor_5 = 0.4

# Calculamos la probabilidad a posteriori de que un número sea mayor que 5
prob_mayor_5 = sum(numeros > 5) / len(numeros)
prob_posteriori_mayor_5 = (prob_mayor_5 * prob_priori_mayor_5) / ((prob_mayor_5 * prob_priori_mayor_5) + ((1 - prob_mayor_5) * (1 - prob_priori_mayor_5)))

print("La probabilidad a priori de que un número sea mayor que 5 es:", prob_priori_mayor_5)
print("La probabilidad a posteriori de que un número sea mayor que 5 es:", prob_posteriori_mayor_5)


"""
 En este ejemplo, suponemos que la probabilidad a priori de que un número sea mayor que 5 es de 0.4.
 Luego, calculamos la probabilidad a posteriori de que un número elegido al azar sea mayor que 5, 
 utilizando la fórmula de Bayes. La salida es un número entre 0 y 1 que representa la probabilidad 
 a posteriori de que un número elegido al azar sea mayor que 5, teniendo en cuenta tanto los datos 
 observados como la información a priori.
"""
