# Importamos la biblioteca necesaria
import numpy as np

# Definimos los estados posibles del tiempo. En este caso, consideramos dos estados posibles: lluvia (R) y no lluvia (N).
estados = ["R", "N"]

# Definimos los observables posibles. En este caso, consideramos dos observables posibles: paraguas (U) y sin paraguas (N).
observables = ["U", "N"]

# Definimos las probabilidades iniciales de estar en cada estado. En este caso, consideramos que hay un 50% de probabilidad de que esté lloviendo o no.
probabilidad_inicial = np.array([0.5, 0.5])

# Definimos la matriz de transición de estados. En este caso, consideramos que hay un 70% de probabilidad de que si hoy está lloviendo, también lo esté mañana, y un 30% de probabilidad de que mañana no llueva si hoy está lloviendo. De igual manera, consideramos que hay un 80% de probabilidad de que mañana no llueva si hoy no está lloviendo, y un 20% de probabilidad de que sí llueva si hoy no está lloviendo.
probabilidad_transicion = np.array([[0.7, 0.3], [0.2, 0.8]])

# Definimos la matriz de emisión de observables. En este caso, consideramos que si está lloviendo, hay un 60% de probabilidad de que usemos un paraguas y un 40% de probabilidad de que no lo usemos. Si no está lloviendo, hay un 20% de probabilidad de que usemos un paraguas y un 80% de probabilidad de que no lo usemos.
probabilidad_emision = np.array([[0.6, 0.4], [0.2, 0.8]])

# Generamos una secuencia de observaciones aleatorias de longitud 5
longitud_secuencia = 5
secuencia_observaciones = np.zeros(longitud_secuencia, dtype=int)
secuencia_estados_ocultos = np.zeros(longitud_secuencia, dtype=int)
estado_oculto_actual = np.argmax(np.random.multinomial(1, probabilidad_inicial))
for i in range(longitud_secuencia):
    observable_actual = np.argmax(np.random.multinomial(1, probabilidad_emision[estado_oculto_actual]))
    secuencia_observaciones[i] = observable_actual
    secuencia_estados_ocultos[i] = estado_oculto_actual
    estado_oculto_actual = np.argmax(np.random.multinomial(1, probabilidad_transicion[estado_oculto_actual]))

# Imprimimos la secuencia de observaciones y los estados ocultos correspondientes
print("Secuencia de observaciones:", [observables[o] for o in secuencia_observaciones])
print("Estados ocultos correspondientes:", [estados[s] for s in secuencia_estados_ocultos])
# Importamos la biblioteca necesaria
import numpy as np

# Definimos los estados posibles del tiempo. En este caso, consideramos dos estados posibles: lluvia (R) y no lluvia (N).
estados = ["R", "N"]

# Definimos los observables posibles. En este caso, consideramos dos observables posibles: paraguas (U) y sin paraguas (N).
observables = ["U", "N"]

# Definimos las probabilidades iniciales de estar en cada estado. En este caso, consideramos que hay un 50% de probabilidad de que esté lloviendo o no.
probabilidad_inicial = np.array([0.5, 0.5])

# Definimos la matriz de transición de estados. En este caso, consideramos que hay un 70% de probabilidad de que si hoy está lloviendo, también lo esté mañana, y un 30% de probabilidad de que mañana no llueva si hoy está lloviendo. De igual manera, consideramos que hay un 80% de probabilidad de que mañana no llueva si hoy no está lloviendo, y un 20% de probabilidad de que sí llueva si hoy no está lloviendo.
probabilidad_transicion = np.array([[0.7, 0.3], [0.2, 0.8]])

# Definimos la matriz de emisión de observables. En este caso, consideramos que si está lloviendo, hay un 60% de probabilidad de que usemos un paraguas y un 40% de probabilidad de que no lo usemos. Si no está lloviendo, hay un 20% de probabilidad de que usemos un paraguas y un 80% de probabilidad de que no lo usemos.
probabilidad_emision = np.array([[0.6, 0.4], [0.2, 0.8]])

# Generamos una secuencia de observaciones aleatorias de longitud 5
longitud_secuencia = 5
secuencia_observaciones = np.zeros(longitud_secuencia, dtype=int)
secuencia_estados_ocultos = np.zeros(longitud_secuencia, dtype=int)
estado_oculto_actual = np.argmax(np.random.multinomial(1, probabilidad_inicial))
for i in range(longitud_secuencia):
    observable_actual = np.argmax(np.random.multinomial(1, probabilidad_emision[estado_oculto_actual]))
    secuencia_observaciones[i] = observable_actual
    secuencia_estados_ocultos[i] = estado_oculto_actual
    estado_oculto_actual = np.argmax(np.random.multinomial(1, probabilidad_transicion[estado_oculto_actual]))

# Imprimimos la secuencia de observaciones y los estados ocultos correspondientes
print("Secuencia de observaciones:", [observables[o] for o in secuencia_observaciones])
print("Estados ocultos correspondientes:", [estados[s] for s in secuencia_estados_ocultos])
