

from sklearn.feature_extraction.text import TfidfVectorizer

# lista de preguntas
preguntas = ["¿Que es la Inteligencia Artificial?"]

# Crea el objeto de vectorizador TfidfVectorizer
vectorizer = TfidfVectorizer()

# Convierte el texto en una matriz de características numericas basada en la
# frecuencia de los términos y la importancia inversa del documento (TF-IDF).
vector_preguntas = vectorizer.fit_transform(preguntas)

# imprimir la matriz de pesos
print("\n", vector_preguntas.toarray())

# imprimir la lista de palabras en el orden de los pesos
print("\n", vectorizer.get_feature_names_out())
