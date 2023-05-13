

import random

# Parámetros del algoritmo genético
tamano_poblacion = 50
tamano_cromosoma = 10
probabilidad_mutacion = 0.1
num_generaciones = 100

# Función de evaluación (función a optimizar)
def evaluar(cromosoma):
    # Aquí debes implementar la función que evalúa un cromosoma y devuelve su valor de aptitud
    # Cuanto mayor sea el valor de aptitud, mejor será el cromosoma
    # Puedes reemplazar esta función por tu problema específico

    # Ejemplo de función de evaluación (optimización de un número entero)
    valor = int(''.join(map(str, cromosoma)), 2)  # Convertir el cromosoma binario a un número entero
    aptitud = valor ** 2  # Queremos maximizar el cuadrado del número
    return aptitud

# Función de selección (torneo binario)
def seleccion(poblacion):
    seleccionados = []
    for _ in range(len(poblacion)):
        individuo_a = random.choice(poblacion)
        individuo_b = random.choice(poblacion)
        seleccionado = individuo_a if evaluar(individuo_a) > evaluar(individuo_b) else individuo_b
        seleccionados.append(seleccionado)
    return seleccionados

# Función de cruce (cruce en un punto)
def cruce(padre, madre):
    punto_cruce = random.randint(1, tamano_cromosoma - 1)
    hijo = padre[:punto_cruce] + madre[punto_cruce:]
    return hijo

# Función de mutación (mutación de un bit)
def mutacion(cromosoma):
    for i in range(len(cromosoma)):
        if random.random() < probabilidad_mutacion:
            cromosoma[i] = 1 if cromosoma[i] == 0 else 0
    return cromosoma

# Generación de la población inicial
poblacion = []
for _ in range(tamano_poblacion):
    cromosoma = [random.randint(0, 1) for _ in range(tamano_cromosoma)]
    poblacion.append(cromosoma)

# Evolución de la población
for generacion in range(num_generaciones):
    print(f"Generación {generacion + 1}")
    poblacion = seleccion(poblacion)
    nueva_poblacion = []

    while len(nueva_poblacion) < tamano_poblacion:
        padre = random.choice(poblacion)
        madre = random.choice(poblacion)
        hijo = cruce(padre, madre)
        hijo = mutacion(hijo)
        nueva_poblacion.append(hijo)

    poblacion = nueva_poblacion

# Obtener el mejor individuo
mejor_individuo = max(poblacion, key=evaluar)
mejor_valor = int(''.join(map(str, mejor_individuo)), 2)

print("Mejor solución encontrada:")
print(f"Individuo: {mejor_individuo}")
print(f"Valor: {mejor_valor}")
