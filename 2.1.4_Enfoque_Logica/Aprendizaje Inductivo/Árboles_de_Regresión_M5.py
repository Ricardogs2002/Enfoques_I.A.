"""
los árboles de regresión M5 son un modelo de aprendizaje automático útil para hacer predicciones 
numéricas precisas en conjuntos de datos complejos. Al combinar los principios de los árboles de 
decisión y la regresión lineal, el modelo M5 es capaz de generar predicciones precisas mientras se
evita el sobreajuste a los datos de entrenamiento y se manejan los datos faltantes.
"""
import numpy as np               # Importamos numpy para trabajar con arreglos numéricos
import matplotlib.pyplot as plt  # Importamos pyplot de matplotlib para graficar
from sklearn.tree import DecisionTreeRegressor, plot_tree  # Importamos DecisionTreeRegressor y plot_tree de scikit-learn
from sklearn.datasets import make_regression  # Importamos make_regression para generar datos de muestra

# Generamos un conjunto de datos de muestra para la regresión
X, y = make_regression(n_samples=100, n_features=1, noise=10)

# Creamos un árbol de regresión M5 con profundidad máxima de 3
tree = DecisionTreeRegressor(max_depth=3)

# Ajustamos el modelo con los datos de muestra
tree.fit(X, y)

# Creamos un gráfico del árbol resultante
plt.figure(figsize=(8,6))
plot_tree(tree, filled=True, feature_names=["X"], fontsize=10)
plt.show()

"""
En este ejemplo, se crea un conjunto de datos de muestra con una sola variable predictora (n_features=1) y
un nivel de ruido (noise) del 10%. Luego, se crea un árbol de regresión M5 con una profundidad máxima de 3 y 
se ajusta al conjunto de datos de muestra. Finalmente, se muestra un gráfico del árbol resultante utilizando la
función plot_tree de Scikit-learn.
El árbol se compone de nodos de decisión que dividen los datos en subconjuntos y nodos hoja que representan la predicción
numérica final para cada subconjunto.

Cada nodo de decisión está representado por una caja rectangular en el gráfico y contiene información sobre la variable 
de entrada que se utiliza para la división (en este caso, la única variable de entrada es "X"), el valor de corte y el número 
de muestras que pasan por ese nodo. En este ejemplo, el nodo raíz del árbol (en la parte superior del gráfico) divide los datos 
en dos subconjuntos basados en si el valor de "X" es menor o mayor que -1.289.

Cada nodo hoja está representado por una elipse en el gráfico y muestra la predicción numérica para el subconjunto de datos 
correspondiente. En este ejemplo, hay dos nodos hoja que predicen la variable de salida (en este caso, "y") para dos subconjuntos
de datos. El primer nodo hoja (en la parte inferior izquierda del gráfico) predice un valor de salida promedio de -62.31 para 
los datos con "X" menor o igual a -1.289, mientras que el segundo nodo hoja (en la parte inferior derecha del gráfico) predice
un valor de salida promedio de 64.78 para los datos con "X" mayor que -1.289.
