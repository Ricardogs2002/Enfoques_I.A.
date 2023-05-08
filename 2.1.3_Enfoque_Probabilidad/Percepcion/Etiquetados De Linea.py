#Carlos Andres Riveramelo Del Toro
#Etiquetados de linea

#El etiquetado de línea, también conocido como etiquetado de secuencia o etiquetado de tokens
#es una tarea en inteligencia artificial que implica asignar una etiqueta o categoría a cada 
#token o elemento de una secuencia de texto, como palabras, caracteres o partes del habla

"Para correr este programa necesitas la siguiente libreria: pip install nltk"

import nltk

#Descarga los recursos necesarios para el etiquetado de partes del habla
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

#Oración de ejemplo
sentence = "Anita lava la tina."

#Tokenización
tokens = nltk.word_tokenize(sentence)

#Etiquetado de partes del habla
pos_tags = nltk.pos_tag(tokens)

for token, pos_tag in pos_tags:
    print(token, "-", pos_tag)
