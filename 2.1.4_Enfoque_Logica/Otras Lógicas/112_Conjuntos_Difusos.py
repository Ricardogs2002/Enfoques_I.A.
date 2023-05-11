import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Definir los conjuntos difusos

# Definir el rango del universo (dominio)
x = np.arange(0, 11, 1)

# Definir las funciones de pertenencia de los conjuntos difusos
bajo = np.where(x <= 5, 1, 0)
medio = np.where(np.logical_and(x > 0, x < 10), 1, 0)
alto = np.where(x >= 5, 1, 0)

# Paso 2: Visualizar los conjuntos difusos

# Visualizar el conjunto difuso "bajo"
plt.plot(x, bajo, 'r', linewidth=1.5, label='Bajo')

# Visualizar el conjunto difuso "medio"
plt.plot(x, medio, 'g', linewidth=1.5, label='Medio')

# Visualizar el conjunto difuso "alto"
plt.plot(x, alto, 'b', linewidth=1.5, label='Alto')

# Etiquetas de los ejes y leyenda
plt.xlabel('Valores')
plt.ylabel('Pertenencia')
plt.legend()

# Mostrar el gráfico
plt.show()

# Paso 3: Realizar operaciones difusas

# Definir un valor de entrada
valor = 6

# Calcular la pertenencia a cada conjunto difuso
pert_bajo = np.where(x <= 5, 1, 0)
pert_medio = np.where(np.logical_and(x > 0, x < 10), 1, 0)
pert_alto = np.where(x >= 5, 1, 0)

# Paso 4: Tomar decisiones basadas en la lógica difusa

# Definir las reglas difusas
regla1 = np.maximum(pert_bajo, pert_medio)
regla2 = pert_alto

# Calcular el resultado difuso utilizando la operación "OR"
resultado = np.maximum(regla1, regla2)

# Paso 5: Defuzzificar el resultado difuso

# Definir el rango de salida
salida = np.arange(0, 11, 1)

# Desfuzzificar el resultado utilizando el método del centroide
valor_defuzz = np.sum(resultado * salida) / np.sum(resultado)

# Visualizar el resultado difuso y el valor defuzzificado
plt.plot(salida, np.where(salida <= 5, 1, 0), 'k', linewidth=0.5, linestyle='--')
plt.fill_between(salida, np.where(salida <= 5, 1, 0), resultado, alpha=0.7)
plt.plot([valor_defuzz, valor_defuzz], [0, 1], 'r', linewidth=1.5, linestyle='--')
plt.xlabel('Valores')
plt.ylabel('Pertenencia')
plt.title('Resultado Difuso')
plt.show()
