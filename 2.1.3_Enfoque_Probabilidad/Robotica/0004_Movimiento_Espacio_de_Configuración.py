"""
En la robótica, el espacio de configuración se refiere al conjunto de todas las posibles configuraciones o 
estados que puede tomar un robot. En otras palabras, el espacio de configuración es el espacio matemático 
que describe todas las posibles posiciones, orientaciones y velocidades de las articulaciones de un robot.

El espacio de configuración es un concepto importante en la planificación del movimiento de los robots, ya 
que permite modelar y analizar el movimiento de los robots en un espacio matemático abstracto. Por ejemplo, 
si se sabe que un robot tiene seis articulaciones, cada una de las cuales puede girar en un rango de 0 a 360 
grados, el espacio de configuración del robot sería un espacio de seis dimensiones que describe todas las 
posibles combinaciones de ángulos de articulación.


La planificación del movimiento en el espacio de configuración permite a los programadores y diseñadores de 
robots definir trayectorias de movimiento para el robot, evitando obstáculos y optimizando el tiempo de movimiento. 
En general, el espacio de configuración es una herramienta útil para modelar y entender el comportamiento de los 
robots en una variedad de contextos.
"""
import numpy as np
import matplotlib.pyplot as plt

# Definimos los límites del espacio de configuración de cada articulación
limits = [(-np.pi/2, np.pi/2), (-np.pi/2, np.pi/2)]

# Generamos una lista con todas las posibles combinaciones de ángulos de articulación
angles = np.meshgrid(*[np.linspace(l[0], l[1], 50) for l in limits])
angles = np.vstack(list(map(np.ravel, angles))).T

# Calculamos las posiciones de cada articulación en función de los ángulos
x1 = np.cos(angles[:,0])
y1 = np.sin(angles[:,0])
x2 = x1 + np.cos(angles[:,0]+angles[:,1])
y2 = y1 + np.sin(angles[:,0]+angles[:,1])

# Graficamos el rango de movimiento del robot
plt.plot(x1, y1, 'b.', markersize=1)
plt.plot(x2, y2, 'r.', markersize=1)
plt.axis('equal')
plt.show()
