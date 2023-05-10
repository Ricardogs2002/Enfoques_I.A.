# Importar la biblioteca NumPy
import numpy as np
import matplotlib.pyplot as plt
# Crear una lista de valores para el eje x
x = np.linspace(0, 2*np.pi, 100)

# Crear dos listas de valores para los ejes y
y1 = np.sin(x)
y2 = np.cos(x)

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Añadir las dos curvas al conjunto de ejes
ax.plot(x, y1, label="sin(x)")
ax.plot(x, y2, label="cos(x)")

# Configurar la leyenda
ax.legend()

# Configurar el título del gráfico
ax.set_title("Funciones seno y coseno")

# Configurar la etiqueta del eje x
ax.set_xlabel("x")

# Configurar la etiqueta del eje y
ax.set_ylabel("y")

# Mostrar el gráfico
plt.show()
