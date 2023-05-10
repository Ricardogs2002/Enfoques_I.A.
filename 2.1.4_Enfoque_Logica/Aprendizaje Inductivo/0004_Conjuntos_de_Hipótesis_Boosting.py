from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargamos el dataset de iris
iris = load_iris()

# Dividimos los datos en conjuntos de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(iris.data, iris.target, test_size=0.2)

# Creamos un clasificador de árbol de decisión como hipótesis débil
clf_arbol_decision = DecisionTreeClassifier(max_depth=1)

# Creamos un clasificador AdaBoost y lo ajustamos al conjunto de entrenamiento
clf_boosting = AdaBoostClassifier(base_estimator=clf_arbol_decision, n_estimators=100, learning_rate=1.0)
clf_boosting.fit(X_entrenamiento, y_entrenamiento)

# Realizamos predicciones en el conjunto de prueba y calculamos la precisión
y_prediccion = clf_boosting.predict(X_prueba)
precision = accuracy_score(y_prueba, y_prediccion)

print("Precisión: {:.2f}%".format(precision*100))
