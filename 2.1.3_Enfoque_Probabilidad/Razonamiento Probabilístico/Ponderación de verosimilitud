from sklearn import linear_model

# Crear un modelo de regresión lineal
reg = linear_model.LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
reg.fit(X_train, y_train)

# Predecir los valores para los datos de prueba
y_pred = reg.predict(X_test)

# Calcular la verosimilitud de los valores de prueba
likelihood = reg.score(X_test, y_test)

# Imprimir la verosimilitud
print("Verosimilitud:", likelihood)

"""
El resultado de 0.56690456157377 es el 
coeficiente de determinación R², que es una medida 
de la verosimilitud del modelo de regresión 
lineal. R² representa la proporción de la variación en 
la variable de respuesta (en este caso, y) que es 
explicada por el modelo.
"""

"""
La ponderación de la verosimilitud es una técnica 
utilizada en la inteligencia artificial para mejorar la 
precisión y la fiabilidad de los modelos de aprendizaje automático. 
La verosimilitud es una medida de la probabilidad de que un 
conjunto de datos observados sea generado por un modelo en particular.
"""
