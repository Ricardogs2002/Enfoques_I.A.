!pip install scikit-learn

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Paso 1: Preparar los datos de entrenamiento y etiquetas
X = [[1, 2], [2, 3], [3, 3], [2, 1], [3, 2]]  # Datos de entrenamiento
y = [0, 0, 0, 1, 1]  # Etiquetas correspondientes a los datos

# Paso 2: Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 3: Crear una instancia de la Máquina de Vectores de Soporte
svm = SVC(kernel='linear')

# Paso 4: Entrenar la SVM
svm.fit(X_train, y_train)

# Paso 5: Realizar predicciones en el conjunto de prueba
y_pred = svm.predict(X_test)

# Paso 6: Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión:", accuracy)

#Paso 1: Preparar los datos de entrenamiento y etiquetas

#Definimos X como una matriz de características. Cada fila representa una muestra y cada columna representa una característica.
#Definimos y como una lista de etiquetas correspondientes a cada muestra en X.
#Paso 2: Dividir los datos en conjunto de entrenamiento y prueba

#Utilizamos la función train_test_split de scikit-learn para dividir los datos X y las etiquetas y en conjuntos de entrenamiento y prueba.
#El parámetro test_size indica el porcentaje de datos que se utilizarán como conjunto de prueba.
#Paso 3: Crear una instancia de la Máquina de Vectores de Soporte

#Creamos una instancia de SVC (Support Vector Classifier) que representa la Máquina de Vectores de Soporte.
#En este ejemplo, utilizamos un kernel lineal especificado con kernel='linear'. Puedes experimentar con otros tipos de kernel, como 'rbf' o 'poly'.
#Paso 4: Entrenar la SVM

#Utilizamos el método fit para entrenar la SVM con los datos de entrenamiento X_train y las etiquetas correspondientes y_train.
#Paso 5: Realizar predicciones en el conjunto de prueba

#"Utilizamos el método predict para realizar predicciones en el conjunto de prueba X_test.
#Paso 6: Calcular la precisión del modelo

#Utilizamos la función accuracy_score de scikit-learn para calcular la precisión del modelo comparando las etiquetas predichas y_pred con las etiquetas reales y_test.
#La precisión se imprime en la consola.
