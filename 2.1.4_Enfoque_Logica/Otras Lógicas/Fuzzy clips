import numpy as np
from sklearn.datasets import load_iris   # importar el conjunto de datos de iris desde scikit-learn
from sklearn.model_selection import train_test_split  # importar la función train_test_split de scikit-learn
from sklearn.metrics import accuracy_score  # importar la función accuracy_score de scikit-learn para evaluar la precisión del modelo
from sklearn.neighbors import KNeighborsClassifier  # importar el clasificador de vecinos más cercanos de scikit-learn

# Cargar el dataset de iris
iris = load_iris()

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)

# Definir el modelo de clasificación difusa
model = KNeighborsClassifier(n_neighbors=3)  # crear un modelo de clasificación de vecinos más cercanos con 3 vecinos
model.fit(X_train, y_train)  # entrenar el modelo en los datos de entrenamiento

# Predecir las clases para los datos de prueba
y_pred = model.predict(X_test)  # predecir las clases para los datos de prueba

# Evaluar la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)  # calcular la precisión del modelo comparando las etiquetas de clase verdaderas y predichas
print('Precisión del modelo:', accuracy)  # imprimir la precisión del modelo en la consola

"""
Los Fuzzy Clips (o Fuzzy Expert Systems) son una
técnica de inteligencia artificial que se utiliza para 
construir sistemas expertos que imitan el proceso de toma de decisiones humanas.
La técnica se basa en la teoría de conjuntos difusos, 
que es una extensión de la teoría de conjuntos tradicional 
para lidiar con la incertidumbre. En lugar de tener conjuntos 
bien definidos, los conjuntos difusos tienen miembros que tienen 
grados de pertenencia borrosos.
"""
