import numpy as np

# Creamos un pequeño corpus de ejemplo
spanish_corpus = ["el perro corre en el parque",
                  "la gata duerme en el sillón",
                  "el niño juega con el balón"]

english_corpus = ["the dog runs in the park",
                  "the cat sleeps on the couch",
                  "the boy plays with the ball"]

# Creamos diccionarios de palabras para cada idioma
español = set([word for sentence in spanish_corpus for word in sentence.split()])
ingles = set([word for sentence in english_corpus for word in sentence.split()])

# Creamos una tabla de frecuencias de palabras
freq_table = np.zeros((len(español), len(ingles)))
for i, palabra_es in enumerate(español):
    for j, palabra_in in enumerate(ingles):
        count = 0
        for k in range(len(spanish_corpus)):
            if palabra_es in spanish_corpus[k] and palabra_in in english_corpus[k]:
                count += 1
        freq_table[i][j] = count

# Normalizamos la tabla de frecuencias
for i in range(len(español)):
    freq_table[i] /= freq_table[i].sum()

# Definimos una función para traducir una frase del español al inglés
def traduce(oracion):
    oracion_in = []
    for english_sentence in english_corpus:
        probabilidad = 1
        for palabra_es in oracion.split():
            # Calculamos la probabilidad de cada palabra en la oración española
            if palabra_es in español:
                max_prob = max(freq_table[list(español).index(palabra_es)])
                probabilidad *= max_prob
        for palabra_in in english_sentence.split():
            # Calculamos la probabilidad de cada palabra en la oración en inglés
            if palabra_in in ingles:
                probabilidad *= freq_table[:,list(ingles).index(palabra_in)].max()
        # Agregamos la oración en inglés y su probabilidad a una lista
        oracion_in.append((english_sentence, probabilidad))
    # Devolvemos la oración en inglés con la probabilidad más alta
    return max(oracion_in, key=lambda x: x[1])[0]

# Probamos el algoritmo con una frase de ejemplo
oracion = "el perro corre en el parque"
traduccion = traduce(oracion)
print(f"Traducción de '{oracion}' al inglés: {traduccion}")


