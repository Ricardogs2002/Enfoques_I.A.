import nltk

def syntactic_analysis(sentence):
    # Definir la gramática para el análisis sintáctico
    grammar = nltk.CFG.fromstring("""
        S -> NP VP '.'
        NP -> DT NN
        VP -> V NP
        DT -> 'The' | 'the'
        NN -> 'cat' | 'dog'
        V -> 'chased'
    """)

    # Crear un analizador sintáctico
    parser = nltk.ChartParser(grammar)

    # Tokenizar la oración en palabras
    tokens = nltk.word_tokenize(sentence)
    tagged_tokens = nltk.pos_tag(tokens)

    # Obtener solo las palabras de los tokens etiquetados
    words = [tagged_token[0] for tagged_token in tagged_tokens]

    # Realizar el análisis sintáctico de la oración
    for tree in parser.parse(words):
        tree.pretty_print()

# Oración de ejemplo
sentence = "The cat chased the dog."

# Realizar el análisis sintáctico de la oración
syntactic_analysis(sentence)
