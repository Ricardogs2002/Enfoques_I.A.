

import spacy
from nltk.corpus import wordnet as wn


"spaCy:"# Es una librería de procesamiento del lenguaje natural en Python y Cython.
# Ofrece pipelines preentrenados y soporte para más de 70 idiomas.(teoria porque en español no pude)
#Proporciona componentes para el reconocimiento de entidades,
# etiquetado de partes de la oración, análisis de dependencias, 
#clasificación de texto, entre otros.

"nltk.wsd:" #Es un módulo de NLTK (Natural Language Toolkit) que contiene algoritmos
# para la desambiguación del sentido de las palabras.
# La desambiguación del sentido de las palabras consiste en asignar el significado
# correcto a una palabra en un contexto determinado.
# El módulo nltk.wsd incluye la implementación del algoritmo de Lesk,
# que utiliza la superposición de definiciones entre palabras.

"nltk.corpus:"# Es otro módulo de NLTK que contiene recursos lingüísticos como corpus
#, léxicos y ontologías. Un corpus es una colección de textos anotados o etiquetados
#, mientras que un léxico es un conjunto de palabras y sus significados. 
#El módulo nltk.corpus permite acceder a diversos recursos, incluido WordNet, 
#una base de datos léxica que contiene grupos de sinónimos (synsets) y relaciones semánticas.

"Nota en teoria deberia funcionar para el español pero no logre hacerlo"
# Cargar el modelo de spaCy para inglés
nlp = spacy.load("es_core_news_sm")#Nota para que la libreira de spacy de la respuesta en español
#debe ser es_core_news_sm

# Definir la oración a analizar
sentence = "I bought a mouse for my computer"

# Analizar la oración con spaCy y obtener el objeto Doc
doc = nlp(sentence)

# Mostrar las entidades reconocidas por spaCy
print("////////////////Entidades:")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Mostrar las dependencias sintácticas reconocidas por spaCy
print("//////////////Dependencias:")
for token in doc:
    print(token.text, token.dep_, token.head.text)

# Mostrar los posibles significados de cada palabra utilizando WordNet
print("////////////////Significados:")
for token in doc:
    synsets = wn.synsets(token.text)
    print(token.text, [synset.definition() for synset in synsets])

# Analizar el sentido de cada palabra utilizando TextBlob
print("Desambiguación:")
for token in doc:
    if token.pos_ == "NOUN":
        synsets = wn.synsets(token.text)
        print(token.text, synsets[0].definition() if synsets else "No encontrado")
    else:
        print(token.text, "No aplicable")
