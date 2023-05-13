import nltk
import numpy as np

def extract_entities(text):
    # Tokeniza el texto en oraciones
    sentences = nltk.sent_tokenize(text)
    # Tokeniza cada oración en palabras
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    # Etiqueta gramaticalmente cada palabra en las oraciones
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    # Aplica el etiquetado de entidades nombradas a las oraciones
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
    
    entities = []
    for tree in chunked_sentences:
        # Extrae las entidades nombradas del árbol de etiquetado
        entities.extend(extract_entity_names(tree))
    
    return entities

def extract_entity_names(t):
    entity_names = []
    
    if hasattr(t, 'label') and t.label():
        # Verifica si el nodo actual tiene una etiqueta de entidad nombrada
        if t.label() == 'NE':
            # Si es así, agrega la entidad a la lista de nombres de entidad
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            # Si no es una entidad nombrada, busca entidades en los hijos del nodo
            for child in t:
                entity_names.extend(extract_entity_names(child))
    
    return entity_names

# Texto de ejemplo
text = "Barack Obama was born in Hawaii and became the 44th President of the United States."

# Realizar la extracción de entidades nombradas
entities = extract_entities(text)

# Mostrar las entidades encontradas
print("Entidades encontradas:")
for entity in entities:
    print(entity)
