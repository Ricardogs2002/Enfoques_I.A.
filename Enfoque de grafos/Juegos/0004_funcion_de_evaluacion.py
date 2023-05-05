import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo aleatorio con 50 nodos y probabilidad de conexión de 0.2
G = nx.gnp_random_graph(50, 0.2)

# Calcular la distribución de grados de los nodos del grafo
grados = nx.degree_histogram(G)

# Visualizar la distribución de grados de los nodos en un histograma
plt.hist(grados, bins=range(len(grados)+1), align='left')
plt.xlabel('Grado')
plt.ylabel('Número de nodos')
plt.show()

"""

La función de evaluación en el enfoque de grafos en Python se utiliza para evaluar la calidad de un modelo de 
aprendizaje automático que utiliza un grafo como entrada. En general, esta función mide el grado de ajuste entre 
las predicciones del modelo y los valores reales del problema que se está resolviendo, y se utiliza para ajustar 
los parámetros del modelo y mejorar su rendimiento. Hay varias métricas que se pueden utilizar como función de evaluación
en el enfoque de grafos, como la precisión, el recall, la F1-score, el área bajo la curva ROC, entre otros. La elección de la 
métrica adecuada dependerá del problema específico que se esté resolviendo. En Python, se pueden utilizar librerías como scikit-learn, 
TensorFlow o PyTorch para implementar diferentes funciones de evaluación en el enfoque de grafos.
