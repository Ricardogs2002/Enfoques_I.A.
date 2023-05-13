import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
#Paso 1: Generar datos de muestra
#En lugar de cargar un archivo CSV, generaremos datos de muestra directamente
#en el código. Usaremos la función numpy.random.rand() para generar números 
#aleatorios y crear un DataFrame de Pandas.
# Generar datos de muestra

np.random.seed(10)  # Para obtener los mismos resultados cada vez que ejecutes el programa
n_samples = 100  # Número de muestras
n_variables = 5  # Número de variables predictoras

data = pd.DataFrame(np.random.rand(n_samples, n_variables + 1),
                    columns=['Variable' + str(i) for i in range(n_variables)] + ['Variable_objetivo'])

print(data.head())

#Paso 2: Dividir los datos en conjuntos de entrenamiento y prueba
#Dividiremos los datos generados en conjuntos de entrenamiento 
#y prueba utilizando la función train_test_split de sklearn.
# Dividir datos en entrenamiento y prueba

train_data, test_data = train_test_split(data, test_size=0.3, random_state=0)

#Paso 3: Entrenar un modelo de referencia
#Al igual que en el enfoque anterior, entrenaremos un modelo de 
#referencia (usando RandomForestRegressor en este caso) en nuestro conjunto 
#de entrenamiento y evaluaremos su rendimiento en el conjunto de prueba.
# Seleccionar la variable objetivo
target_variable = 'Variable_objetivo'

# Definir variables predictoras
predictors = [x for x in train_data.columns if x != target_variable]

# Entrenar modelo de referencia
rf = RandomForestRegressor(n_estimators=100, random_state=0)
rf.fit(train_data[predictors], train_data[target_variable])

# Evaluar modelo de referencia en conjunto de prueba
rf_score = rf.score(test_data[predictors], test_data[target_variable])
print("R^2 score del modelo de referencia:", rf_score)

#Paso 5: Calcular la importancia de las variables y eliminar las menos importantes
#Calcularemos la importancia de cada variable y eliminaremos las variables 
#cuya importancia sea menor al valor medio de importancia.

# Calcular importancia de variables
importances = pd.DataFrame({'Variable': predictors, 'Importancia': rf.feature_importances_})
importances = importances.sort_values('Importancia', ascending=False)

# Calcular umbral de eliminación
importance_threshold = importances['Importancia'].mean()

# Seleccionar variables a eliminar
variables_a_eliminar = importances[importances['Importancia'] < importance_threshold]['Variable'].tolist()

# Eliminar variables del conjunto de datos
train_data = train_data.drop(variables_a_eliminar, axis=1)
test_data = test_data.drop(variables_a_eliminar, axis=1)

print("Variables eliminadas:", variables_a_eliminar)
print("Nuevo conjunto de entrenamiento:\n", train_data.head())
print("Nuevo conjunto de prueba:\n", test_data.head())
