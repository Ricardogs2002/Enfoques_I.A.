
#Sintaxis y Semantica: Cuantificadores

#este programa utiliza el "Natural Language Toolkit" para realizar un analisis sintatico

"Para correr este programa necesitas la siguiente libreria: pip install nltk"

import nltk

#Descarga los recursos necesarios para el análisis sintáctico
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

#Oración de ejemplo
sentence = "Anita sigue lavando la pinshe tina"

#Tokenización
tokens = nltk.word_tokenize(sentence)

#Análisis sintáctico
tagged_tokens = nltk.pos_tag(tokens)

#Extracción de cuantificadores
quantifiers = ['Anita', 'sigue', 'lavando', 'la', 'pinshe', 'tina']

extracted_quantifiers = []
for token, pos_tag in tagged_tokens:
    if token.lower() in quantifiers:
        extracted_quantifiers.append(token)

print("cuantificadores en la oracion:")
for quantifier in extracted_quantifiers:
    print(quantifier)
