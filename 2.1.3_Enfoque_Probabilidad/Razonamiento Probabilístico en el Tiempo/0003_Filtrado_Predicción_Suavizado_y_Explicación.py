import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Crear un conjunto de datos de ejemplo
datos = np.sin(np.arange(0, 6*np.pi, 0.1)) + np.random.randn(189) * 0.2

# Convertir los datos a un objeto DataFrame de Pandas
datos_df = pd.DataFrame(datos, columns=['y'])

# Aplicar un filtrado de media móvil para suavizar los datos
suavizado = datos_df.rolling(window=5).mean().dropna().values.flatten()

# Dividir los datos en un conjunto de entrenamiento y un conjunto de prueba
datos_entrenamiento = datos[:80]
datos_prueba = datos[80:]

# Ajustar un modelo de regresión lineal a los datos de entrenamiento
X_entrenamiento = np.arange(len(datos_entrenamiento)).reshape(-1, 1)
y_entrenamiento = datos_entrenamiento.reshape(-1, 1)
modelo = LinearRegression()
modelo.fit(X_entrenamiento, y_entrenamiento)

# Realizar predicciones en el conjunto de prueba utilizando el modelo ajustado
X_prueba = np.arange(len(datos_entrenamiento), len(datos))
y_prueba_pred = modelo.predict(X_prueba.reshape(-1, 1)).flatten()

# Calcular el error de predicción
y_prueba = datos_prueba.reshape(-1, 1)
rmse = np.sqrt(np.mean((y_prueba - y_prueba_pred)**2))

# Visualizar los datos originales, suavizados y predichos
plt.plot(datos, label='Datos originales')
plt.plot(np.arange(2, len(suavizado)+2), suavizado, label='Datos suavizados')
plt.plot(np.arange(80, len(datos)), y_prueba_pred, label='Predicción')
plt.legend()
plt.show()

# Calcular el coeficiente de correlación entre los datos originales y suavizados
coef_corr = np.corrcoef(datos, suavizado)[0,1]

# Imprimir los resultados
print('Error de predicción: {:.2f}'.format(rmse))
print('Coeficiente de correlación: {:.2f}'.format(coef_corr))

