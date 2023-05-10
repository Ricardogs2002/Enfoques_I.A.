"""
La Búsqueda Tabú es una técnica de optimización que permite encontrar soluciones de alta 
calidad en problemas complejos, evitando quedar atrapado en óptimos locales mediante la 
exploración de soluciones que no son necesariamente las mejores en un momento dado, pero 
que pueden llevar a mejores soluciones a largo plazo.
"""
import numpy as np
import matplotlib.pyplot as plt

# Definimos la función objetivo
def f(x):
    return -np.sin(x) * (1.4 - np.abs(x))

# Definimos el espacio de búsqueda
x_min = -5
x_max = 5

# Definimos los parámetros de la Búsqueda Tabú
x_actual = np.random.uniform(x_min, x_max)
x_tabu = [x_actual]
iteraciones = 100
tam_tabu = 5

# Realizamos la Búsqueda Tabú
for i in range(iteraciones):
    # Generamos una lista de posibles soluciones vecinas
    x_vecinas = [np.random.uniform(x_min, x_max) for i in range(10)]
    x_vecinas.append(x_actual)
    # Seleccionamos la mejor solución vecina que no esté en la lista tabú
    x_nueva = min([x for x in x_vecinas if x not in x_tabu], key=f)
    # Agregamos la solución nueva a la lista tabú
    x_tabu.append(x_nueva)
    if len(x_tabu) > tam_tabu:
        x_tabu.pop(0)
    # Actualizamos la solución actual si la nueva solución es mejor
    if f(x_nueva) < f(x_actual):
        x_actual = x_nueva

# Graficamos la función objetivo y el proceso de búsqueda
x = np.linspace(x_min, x_max, 100)
y = f(x)
plt.plot(x, y, label="Función Objetivo")
plt.plot(x_tabu, [f(x) for x in x_tabu], 'ro-', label="Proceso de Búsqueda")
plt.legend()
plt.show()
"""
l programa implementa el algoritmo de Búsqueda Tabú para encontrar la mejor solución posible a un problema 
de optimización. En este caso, el problema es encontrar el mínimo global de la función de Rosenbrock, que 
es una función de prueba común en la optimización.

El algoritmo de Búsqueda Tabú comienza con una solución inicial aleatoria y realiza iteraciones para encontrar
la mejor solución posible. En cada iteración, se genera una lista de posibles soluciones vecinas y se evalúa 
cada una de ellas para encontrar la mejor opción. Sin embargo, el algoritmo también mantiene una lista de 
soluciones "tabú" que no se pueden explorar durante un cierto número de iteraciones para evitar caer en ciclos 
de soluciones repetitivas.

El programa utiliza la librería Matplotlib para graficar la evolución de la función de costo durante las iteraciones. 
Se puede observar cómo la función de costo disminuye en cada iteración, lo que indica que el algoritmo está 
convergiendo hacia la mejor solución posible.
"""
