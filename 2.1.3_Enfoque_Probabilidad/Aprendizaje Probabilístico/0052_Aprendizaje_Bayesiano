# Areli Sarai García Medina | 20310380
# Aprendizaje Bayesiano

from collections import Counter

# Definir un conjunto de datos de lanzamientos de moneda
datos = ['cara', 'cruz', 'cruz', 'cara', 'cruz', 'cara', 'cara', 'cruz', 'cruz', 'cruz', 'cruz', 'cara', 'cruz']

# Contar la frecuencia de cada resultado
frecuencias = Counter(datos)

# Calcular la probabilidad previa de obtener cara o cruz
total = len(datos)
probabilidad_cara = frecuencias['cara'] / total
probabilidad_cruz = frecuencias['cruz'] / total

# Definir una función para actualizar las probabilidades a partir de un nuevo lanzamiento
def actualizar_probabilidades(resultados, probabilidad_cara, probabilidad_cruz):
    frecuencias = Counter(resultados)
    total = len(resultados)
    nueva_probabilidad_cara = frecuencias['cara'] / total
    nueva_probabilidad_cruz = frecuencias['cruz'] / total
    probabilidad_cara = (probabilidad_cara * total + nueva_probabilidad_cara) / (total + 1)
    probabilidad_cruz = (probabilidad_cruz * total + nueva_probabilidad_cruz) / (total + 1)
    return probabilidad_cara, probabilidad_cruz

# Hacer una serie de lanzamientos y actualizar las probabilidades después de cada uno
for i in range(10):
    resultado = 'cara'  # Aquí se simula el lanzamiento de la moneda (cara o cruz)
    probabilidad_cara, probabilidad_cruz = actualizar_probabilidades([resultado], probabilidad_cara, probabilidad_cruz)
    print(f"Después del lanzamiento {i+1}, la probabilidad de obtener cara es {probabilidad_cara:.2f} y la probabilidad de obtener cruz es {probabilidad_cruz:.2f}")
