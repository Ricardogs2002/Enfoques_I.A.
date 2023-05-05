# Implementación de Vigilancia de Ejecución y Replanificación con ejemplo de un robot y obstaculos

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# Para ver los plots en tiempo real en Spyder, se necesita utilizar TkAgg como backend
matplotlib.use('TkAgg') 

# Crear un camino aleatorio para el robot
path = np.random.rand(10, 2).astype(np.float64) * 10 - 5

# Inicializar el estado del robot
robotPos = np.array([0, 0], dtype=np.float64)
tolerance = 0.1 # La distancia que el robot puede estar del objetivo y aún considerarse "llegado"
safetyDistance = 0.5  # Distancia de seguridad para detectar obstáculos
# Definir las coordenadas de los obstáculos en el espacio 2D y crear un array NumPy
obstacles = np.array([[2, 2], [2, -2], [-2, 2], [-2, -2]], dtype=np.float64)

# Visualizar el camino, los obstáculos y el progreso del robot en tiempo real
fig, ax = plt.subplots()
ax.plot(path[:, 0], path[:, 1], 'b--', label='Camino planificado') # Dibujar el camino planificado en azul
ax.plot(obstacles[:, 0], obstacles[:, 1], 'ks', label='Obstáculos') # Dibujar los obstáculos en negro
ax.plot(robotPos[0], robotPos[1], 'ro', label='Robot') # Dibujar el robot en rojo
ax.legend()

# Iterar a través del camino planificado
for i in range(len(path)):
    targetPos = path[i] # Obtener la siguiente posición objetivo en el camino
    while np.linalg.norm(robotPos - targetPos) > tolerance: # Mientras el robot no haya llegado al objetivo
        # Calcular la distancia entre el robot y los obstáculos
        distances = np.linalg.norm(robotPos - obstacles, axis=1)
        if np.any(distances < safetyDistance): # Si el robot detecta un obstáculo
            print("¡Obstáculo detectado! Replanificando...")
            # Replanificar una nueva ruta alrededor del obstáculo
            newTargetPos = path[i]
            while np.linalg.norm(robotPos - newTargetPos) > tolerance: # Mientras el robot no haya llegado al nuevo objetivo
                # Mover el robot hacia el nuevo objetivo
                robotPos += 0.1 * (newTargetPos - robotPos).astype(np.float64)
                # Actualizar la posición del robot en el gráfico
                ax.lines[2].set_xdata(robotPos[0])
                ax.lines[2].set_ydata(robotPos[1])
                # Actualizar el gráfico en tiempo real
                fig.canvas.draw()
                plt.pause(0.001)
            targetPos = newTargetPos # Actualizar el objetivo original a la nueva posición
        else: # Si no hay obstáculos en el camino
            # Mover el robot hacia la siguiente posición objetivo en el camino
            robotPos += 0.1 * (targetPos - robotPos).astype(np.float64)
            # Actualizar la posición del robot en el gráfico
            ax.lines[2].set_xdata(robotPos[0])
            ax.lines[2].set_ydata(robotPos[1])
            # Actualizar el gráfico en tiempo real
            fig.canvas.draw()
            plt.pause(0.001)

plt.show()
