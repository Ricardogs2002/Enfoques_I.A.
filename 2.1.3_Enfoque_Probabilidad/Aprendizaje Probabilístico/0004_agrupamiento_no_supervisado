from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Generamos un conjunto de datos aleatorios para agrupar
X = np.random.rand(100, 2)
print(X)
# Creamos un objeto AgglomerativeClustering con 3 clústeres
agg_clustering = AgglomerativeClustering(n_clusters=3)

# Ajustamos el modelo a los datos
agg_clustering.fit(X)

# Obtenemos las etiquetas de clústeres para cada punto de datos
labels = agg_clustering.labels_

# Imprimimos los resultados

print("Etiquetas de clústeres: ", labels)
