
# Dinámica y Control

import numpy as np # Se utiliza principalmente para trabajar con arreglos multidimensionales
import matplotlib.pyplot as plt # Se utiliza para crear gráficos y visualizaciones a partir de los datos que se encuentran en arreglos

# Parámetros del sistema
m = 7.0  # masa del objeto
k = 5.0  # constante del resorte
b = 0.3  # coeficiente de amortiguamiento

# Condiciones iniciales
x0 = 2.0  # posición inicial
v0 = 0.0  # velocidad inicial

# Tiempo de simulación
t_final = 15.0  # segundos
dt = 0.03  # segundos

# Función que define las ecuaciones de dinámica del sistema
def dinamica(t, y):
    x, v = y
    dxdt = v
    dvdt = (-k * x - b * v) / m
    return [dxdt, dvdt]

# Integración numérica utilizando el método de Euler
t = 0.0
x = x0
v = v0
trayectoria = [[t, x, v]]
while t < t_final:
    y = [x, v]
    dydt = dinamica(t, y)
    x += dydt[0] * dt
    v += dydt[1] * dt
    t += dt
    trayectoria.append([t, x, v])
trayectoria = np.array(trayectoria)

# Visualización de resultados
plt.plot(trayectoria[:, 0], trayectoria[:, 1], label='Posición')
plt.plot(trayectoria[:, 0], trayectoria[:, 2], label='Velocidad')
plt.legend()
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición/Velocidad')
plt.show()
