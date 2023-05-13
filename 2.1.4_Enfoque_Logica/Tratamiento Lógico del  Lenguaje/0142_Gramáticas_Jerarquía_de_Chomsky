
# Gramáticas: Jerarquía de Chomsky

# Definimos la gramática en forma normal de Chomsky
gramatica = {
    "S": [["NP", "VP"]],   # Regla de producción de la forma S -> NP VP
    "NP": [["Det", "Noun"], ["Det", "Adj", "Noun"]],   # Reglas de producción de la forma NP -> Det Noun y NP -> Det Adj Noun
    "VP": [["Verb", "NP"]],   # Regla de producción de la forma VP -> Verb NP
    "Det": ["el", "la", "los", "las"],   # Terminales para el símbolo Det
    "Adj": ["rojo", "verde", "grande", "pequeño"],   # Terminales para el símbolo Adj
    "Noun": ["perro", "gato", "pájaro", "árbol"],   # Terminales para el símbolo Noun/Objeto
    "Verb": ["corre", "salta", "camina"]   # Terminales para el símbolo Verbo
}

# Definimos la función para realizar el análisis sintáctico
def analizar_oracion(oracion):
    # Convertimos la oración en una lista de palabras
    palabras = oracion.split()
    # Creamos una lista de posibles expansiones para cada palabra
    posibles_expansiones = []
    for palabra in palabras:
        expansiones = []
        # Buscamos en la gramática las expansiones posibles para la palabra
        for simbolo, expansiones_simbolo in gramatica.items():
            for expansion in expansiones_simbolo:
                if palabra in expansion:
                    expansiones.append((simbolo, expansion))
        posibles_expansiones.append(expansiones)
    # Creamos una tabla de análisis sintáctico
    tabla = [[set() for _ in range(len(palabras) + 1)] for _ in range(len(palabras) + 1)]
    # Agregamos las posibles expansiones de longitud 1 a la tabla
    for i in range(len(palabras)):
        for simbolo, expansion in posibles_expansiones[i]:
            tabla[i][i+1].add((simbolo, expansion))
    # Agregamos las posibles expansiones de longitud >1 a la tabla
    for longitud in range(2, len(palabras) + 1):
        for i in range(len(palabras) - longitud + 1):
            j = i + longitud
            for k in range(i+1, j):
                for simbolo1, expansion1 in tabla[i][k]:
                    for simbolo2, expansion2 in tabla[k][j]:
                        if (simbolo1, simbolo2) in gramatica:
                            for simbolo3, expansion3 in gramatica[(simbolo1, simbolo2)]:
                                tabla[i][j].add((simbolo3, expansion1 + expansion2))
    # Devolvemos la tabla de análisis sintáctico
    return tabla

# Ejemplo de uso de la función para analizar la oración
tabla = analizar_oracion("el perro grande corre")
print(tabla)
