# Areli Sarai García Medina | 20310380
# Gramáticas Probabilísticas Lexicalizadas

import nltk

# Definimos una Gramática Probabilística Lexicalizada
# Utilizamos el formato de string para definir la gramática con probabilidades asociadas a cada regla
# S = Sentence
# NP = Noun Phrase
# VP = Verb Phrase
# V = Verb
# PP = Prepositional Phrase
# P = Preposition
grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    VP -> V NP [0.8] | VP PP [0.2]
    PP -> P NP [1.0]
    V -> 'vió' [0.5] | 'comió' [0.3] | 'caminó' [0.2]
    NP -> 'John' [0.4] | 'Mary' [0.3] | 'Bob' [0.3]
    P -> 'con' [0.6] | 'en' [0.4]
""")

# Definimos un parser CYK con la gramática definida anteriormente
# Un parser es un programa informático que analiza una secuencia de símbolos o tokens
# según una gramática formal y produce una estructura de datos que representa la estructura sintáctica de la secuencia.
parser = nltk.parse.EarleyChartParser(grammar)

# Definimos la oración a analizar como una lista de palabras
sentence = "John vió Mary con Bob".split()

# Analizamos la oración con el parser definido anteriormente
parses = parser.parse(sentence)

# Mostramos los árboles de parseo obtenidos por el parser
for tree in parses:
    print(tree)
