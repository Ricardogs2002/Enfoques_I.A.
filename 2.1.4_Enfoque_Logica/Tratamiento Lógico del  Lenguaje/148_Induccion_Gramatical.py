import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# Oraciones de ejemplo
sentences = [
    "is the cat black.",
    "The dog is brown.",
    "The bird is blue.",
    "The sky is blue.",
    "The grass is green."
]

# Realizar tokenización y etiquetado gramatical
tagged_sentences = [nltk.pos_tag(nltk.word_tokenize(sentence)) for sentence in sentences]
# Utilizamos nltk.word_tokenize para dividir cada oración en una lista de palabras (tokenización)
# Después, aplicamos nltk.pos_tag para etiquetar gramaticalmente cada palabra en la oración

# Obtener reglas gramaticales
grammatical_rules = []
for tagged_sentence in tagged_sentences:
    rules = []
    for (word, pos) in tagged_sentence:
        rules.append((word, pos))
    grammatical_rules.append(rules)
# Iteramos sobre cada oración etiquetada gramaticalmente
# Recorremos cada par (palabra, etiqueta) en la oración etiquetada y lo añadimos a la lista de reglas gramaticales

# Imprimir las reglas gramaticales
for rules in grammatical_rules:
    print(rules)
# Imprimimos las reglas gramaticales para cada oración
