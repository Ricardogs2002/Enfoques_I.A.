"""
Created on Wed Sat 6 2023

@author: Adan Alvarez
"""

import nltk
nltk.download('punkt')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Preprocesamiento de texto
corpus = """
Los chatbots son programas informáticos que han sido diseñados para interactuar con los usuarios de manera natural, simulando una conversación humana. Estos programas pueden ser utilizados para una amplia variedad de tareas, desde proporcionar soporte al cliente hasta vender productos y servicios. La popularidad de los chatbots ha aumentado significativamente en los últimos años debido a los avances en el procesamiento del lenguaje natural y la inteligencia artificial.

El funcionamiento básico de los chatbots se basa en algoritmos que les permiten analizar y procesar el lenguaje natural de los usuarios para luego generar respuestas en tiempo real. Los chatbots utilizan una amplia gama de técnicas de aprendizaje automático para mejorar su capacidad de comprensión del lenguaje natural, incluyendo el uso de redes neuronales y algoritmos de aprendizaje supervisado.

Cuando se les pregunta si son un chatbot, algunos chatbots han sido programados para responder con un "sí" directo, en este caso este chatbot fue creado por Adan Alvarez. Mientras que otros pueden tratar de evadir la pregunta o proporcionar una respuesta humorística. Algunos chatbots incluso pueden ser programados para detectar cuando están siendo interactuados por un humano o por otro chatbot.

Los chatbots también pueden ser programados para responder preguntas específicas basadas en reglas predefinidas o para aprender de manera autónoma a partir de la interacción con los usuarios. Los chatbots que aprenden de manera autónoma utilizan técnicas de aprendizaje por refuerzo para mejorar su capacidad de generar respuestas precisas y relevantes.

Además de su capacidad de procesar el lenguaje natural, los chatbots también pueden ser integrados con otras tecnologías para mejorar su funcionalidad. Por ejemplo, algunos chatbots pueden utilizar la tecnología de reconocimiento de voz para permitir a los usuarios interactuar con ellos utilizando comandos de voz. También pueden ser integrados con sistemas de inteligencia empresarial para proporcionar análisis de datos y recomendaciones a los usuarios.

En resumen, los chatbots son programas informáticos diseñados para interactuar con los usuarios de manera natural, utilizando técnicas de procesamiento del lenguaje natural y aprendizaje automático para analizar y procesar el lenguaje natural de los usuarios y generar respuestas relevantes en tiempo real. Este chatbot fue creado por Adan Alvarez, utilizando las últimas tecnologías de procesamiento de lenguaje natural y aprendizaje automático para proporcionar respuestas precisas y relevantes a las preguntas de los usuarios.
"""

# Toma el texto de entrada y con la funcion sent_tokenize lo convierte a oraciones
sentences = nltk.sent_tokenize(corpus)
# Toma las oraciones guardadas en sentences y las guarda en una lista de palabras ademas de convertirlas a minusculas
word_list = [nltk.word_tokenize(sent.lower()) for sent in sentences]
# Filtra todas las palabras que no sean alfanumericas
word_list_clean = [[word for word in sent if word.isalnum()] for sent in word_list]

# Se crea un objeto y utiliza la técnica de ponderación tf-idf, que asigna un peso a cada palabra en función
# de la frecuencia de aparición en el texto y de la frecuencia de aparición en el conjunto de documentos.
vectorizer = TfidfVectorizer()

# Vectoriza las oraciones volviendo a juntar las palabras pero ahora agregandole peso a cada palabra
X = vectorizer.fit_transform([' '.join(sent) for sent in word_list_clean])

# Hacer una pregunta
query = input("¿Qué te gustaría saber sobre los chatbots? ")

#Convierte la entrada a letras minusculas y de igual manera que las funciones anteriores vectoriza las palabras para agregarles peso
query_vec = vectorizer.transform([query.lower()])

#A partir de la matriz donde se guardo cada palabra de la oracion y sus pesos calcula el vector con el coseno como el vector de entrada sobre los datos almacenados en x
# Como resultado entrega un nuevo vector con los puntajes de similitud
similarity_scores = cosine_similarity(X, query_vec).flatten()

# Obtener respuesta
# Busca el índice en la lista similarity_scores el valor máximo de similitud con la pregunta que se hizo
best_score_index = similarity_scores.argmax()
# Se asigna a la variable answers la respuesta correspondiente con mayor puntaje
answer = sentences[best_score_index]

print("\n\nPregunta: ", query)
print("\nRespuesta: ", answer)
