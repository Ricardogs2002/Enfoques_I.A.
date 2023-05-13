

"//////////////////////////////////////////K-NN/////////////////////////////////////////////////////"

"k-NN (k vecinos más cercanos)"#es un método de clasificación supervisada que asigna una 
#etiqueta a un elemento basándose en las etiquetas de sus k elementos más cercanos en el
#espacio de características1. Por ejemplo, si queremos clasificar una flor según su especie,
#podemos usar k-NN para comparar sus medidas con las de otras flores ya etiquetadas y elegir 
#la etiqueta más frecuente entre las k más cercanas.

"scikit-learn" #Esta es una librería de Python que ofrece herramientas 
#para el aprendizaje automático, como algoritmos de clasificación, regresión, 
#agrupación y reducción de dimensionalidad. Dentro de esta librería, se importa 

"la clase KNeighborsClassifier"#, que es la que implementa el algoritmo k-NN. 
#Esta clase tiene varios métodos, como fit, que sirve para entrenar el modelo 
#con los datos de entrada y salida, y predict, que sirve para predecir la etiqueta
# de un nuevo dato dado sus características.

from sklearn.neighbors import KNeighborsClassifier

# Crear un conjunto de datos de ejemplo
x = [[0, 0], [1, 1], [2, 2], [3, 3]] # Características
y = [0, 0, 1, 1] # Etiquetas

#A continuación, se crea una instancia del clasificador k-NN llamada knn con 
#n_neighbors=3, lo que indica que se utilizarán los 3 vecinos más cercanos 
#para realizar las predicciones.
knn = KNeighborsClassifier(n_neighbors=1)

# Entrenar el modelo con los datos de ejemplo
knn.fit(x, y)

# Predecir la etiqueta de un nuevo dato
print(knn.predict([[1.5, 1.5]])) # Debería imprimir [0]

"//////////////////////////////////////////KMEANS/////////////////////////////////////////////////////"

"k-Medias (k-means)"# es un método de agrupación no supervisada que divide 
#un conjunto de n elementos en k grupos (clusters) según su similitud. 
#Por ejemplo, si queremos agrupar clientes según sus hábitos de compra, 
#podemos usar k-Medias para asignar cada cliente a uno de los k grupos que 
#minimizan la distancia entre el cliente y el centroide del grupo.


from sklearn.cluster import KMeans

#crea una lista de listas llamada X, que contiene 8 puntos bidimensionales 
#(cada punto tiene dos coordenadas). Estos puntos son las características de 
#los datos de ejemplo que se van a agrupar.
# Crear un conjunto de datos de ejemplo
X = [[0, 0], [1, 1], [2, 2], [3, 3], [10, 10], [11, 11], [12, 12], [13, 13]] # Características

#llamado kmeans, que es una instancia de la clase KMeans con el parámetro 
#n_clusters=2. Esto significa que se va a crear un modelo k-Medias con k=2,
# es decir, con dos grupos o clusters.

# Crear el modelo k-Medias con k=2
kmeans = KMeans(n_clusters=2)


#al método fit del objeto kmeans, pasándole como argumento la lista X.
#Esto hace que el modelo k-Medias se entrene con los datos de ejemplo, 
#buscando los dos centroides (los puntos centrales de cada grupo) que minimicen 
#la distancia entre los puntos y sus respectivos grupos.

# Entrenar el modelo con los datos de ejemplo
kmeans.fit(X)

#llama al método predict del objeto kmeans, pasándole como argumento 
#una lista con un punto [[1.5, 1.5]]. Esto hace que el modelo k-Medias
#prediga a qué grupo pertenece ese punto, basándose en su distancia a los centroides. 
# Predecir la etiqueta de un nuevo dato
print(kmeans.predict([[1.5, 1.5]])) # Debería imprimir [0]
print(kmeans.predict([[11.5, 11.5]])) # Debería imprimir [1]

"//////////////////////////////////////////Clustering/////////////////////////////////////////////////////"

"Clustering "#es el proceso general de agrupar elementos en función 
#de algún criterio de similitud o distancia3. Existen diferentes tipos 
#y métodos de clustering, como el clustering jerárquico, el clustering 
#difuso o el método de Ward. El objetivo del clustering es encontrar patrones 
#o estructuras ocultas en los datos que puedan ser útiles para el análisis 
#o la toma de decisiones

# Crear un conjunto de datos de ejemplo
J = [[0, 0], [1, 1], [2, 2], [3, 3], [10, 10], [11, 11], [12, 12], [13, 13]] # Características

# Crear el modelo k-Medias con k=2
kmeans = KMeans(n_clusters=2)

# Entrenar el modelo con los datos de ejemplo
kmeans.fit(J)

# Obtener las etiquetas de los datos de ejemplo
labels = kmeans.labels_
print(labels) # Debería imprimir [0 0 0 0 1 1 1 1]

# Obtener los centroides de los grupos
centroids = kmeans.cluster_centers_
print(centroids) # Debería imprimir [[1.5 1.5] [11.5 11.5]]