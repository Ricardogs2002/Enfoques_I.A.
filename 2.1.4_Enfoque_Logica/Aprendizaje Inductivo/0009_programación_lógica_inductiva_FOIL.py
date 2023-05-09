# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:31:10 2023

@author: Alberto Aguiar
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Definir el conjunto de datos de ejemplo
X = np.array([[1, 'A'],
              [2, 'A'],
              [3, 'B'],
              [4, 'B'],
              [5, 'A']])

y = np.array(['Negativo',
              'Negativo',
              'Positivo',
              'Negativo',
              'Positivo'])

# Convertir variables categóricas en variables numéricas
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
X[:, 1] = label_encoder.fit_transform(X[:, 1])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo de árbol de decisión
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular la precisión de las predicciones
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)
