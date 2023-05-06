import random
import math
import matplotlib.pyplot as plt


# Función para calcular la distancia entre dos ciudades
def distancia(ciudad1, ciudad2):
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Función para calcular el costo de una ruta, es decir, la suma de las distancias entre ciudades consecutivas en la ruta
def ruta_costo(ruta, ciudades):
    costo = 0
    for i in range(len(ruta)):
        costo += distancia(ciudades[ruta[i]], ciudades[ruta[(i + 1) % len(ruta)]])
    return costo

# Función para generar un vecino aleatorio de una ruta dada, intercambiando dos ciudades en posiciones aleatorias
def vecino_aleatorio(ruta):
    # Se eligen dos índices aleatorios para intercambiar
    i = random.randrange(1, len(ruta))
    j = random.randrange(1, len(ruta))
    # Se crea una copia de la ruta sin la ciudad de origen
    ruta_aux = ruta[1:]
    # Se mezcla aleatoriamente la copia de la ruta sin la ciudad de origen
    random.shuffle(ruta_aux)
    # Se crea el vecino intercambiando las ciudades en los índices seleccionados
    vecino = [ruta[0]] + ruta_aux
    vecino[i], vecino[j] = vecino[j], vecino[i]
    return vecino


# Definición de la función recocido_simulado con los siguientes argumentos:
# - ciudades: una lista de tuplas que contiene las coordenadas (x, y) de cada ciudad
# - T_inicial: temperatura inicial para el algoritmo
# - T_final: temperatura final para el algoritmo
# - enfriamiento: constante de enfriamiento para el algoritmo
# - iteraciones: número de iteraciones para el algoritmo
# - ciudad_inicio: índice de la ciudad de inicio de la ruta

# Creamos una ruta inicial que comienza en la ciudad de inicio y pasa por el resto de ciudades de forma aleatoria.
# Luego calculamos su costo actual.
# También inicializamos una mejor ruta y su costo.
def recocido_simulado(ciudades, T_inicial, T_final, enfriamiento, iteraciones, ciudad_inicio):
    ruta_actual = list(range(len(ciudades)))
    ruta_actual.remove(ciudad_inicio)
    random.shuffle(ruta_actual)
    ruta_actual.insert(0, ciudad_inicio)
    costo_actual = ruta_costo(ruta_actual, ciudades)
    mejor_ruta = ruta_actual[:]
    mejor_costo = costo_actual
    
    # Inicializamos la temperatura actual como la temperatura inicial.
    T = T_inicial
    
    # Iteramos por el número de iteraciones especificado.
    for i in range(iteraciones):
        
        # Creamos un vecino aleatorio a partir de la ruta actual.
        vecino = vecino_aleatorio(ruta_actual)
        
        # Calculamos el costo del vecino y la diferencia de costos con la ruta actual.
        costo_vecino = ruta_costo(vecino, ciudades)
        delta_costo = costo_vecino - costo_actual
        
        # Si la diferencia de costos es negativa, el vecino es mejor que la ruta actual, así que lo aceptamos.
        # Si no, calculamos la probabilidad de aceptar el vecino en función de la temperatura actual.
        if delta_costo < 0 or math.exp(-delta_costo / T) > random.uniform(0, 1):
            ruta_actual = vecino[:]
            costo_actual = costo_vecino
        
        # Si la ruta actual es la mejor hasta ahora, actualizamos la mejor ruta y su costo.
        if costo_actual < mejor_costo:
            mejor_ruta = ruta_actual[:]
            mejor_costo = costo_actual
        
        # Cada cierto porcentaje de iteraciones, imprimimos el progreso y dibujamos la mejor ruta hasta ahora.
        if i % (iteraciones // 10) == 0:
            print(f"Progreso: {i / iteraciones * 100:.0f}%")
            print("mejor ruta =\t", mejor_ruta, "costo =\t",mejor_costo)
            dibujar_ruta(ciudades, mejor_ruta, f"Mejor Ruta Encontrada (Costo: {mejor_costo:.2f})")
        
        # Enfriamos la temperatura actual.
        T *= enfriamiento
    
    # Retornamos la mejor ruta y su costo.
    return mejor_ruta, mejor_costo


def dibujar_ruta(ciudades, ruta, titulo=None):
    # Obtenemos las coordenadas en el eje X de cada ciudad en la ruta
    x = [ciudades[i][0] for i in ruta]
    # Obtenemos las coordenadas en el eje Y de cada ciudad en la ruta
    y = [ciudades[i][1] for i in ruta]
    # Dibujamos la ruta en el gráfico, utilizando círculos como marcadores y una línea continua para unirlos
    plt.plot(x, y, 'co-')
    # Añadimos un número a cada ciudad en la ruta, para identificarla en el gráfico
    for i, ciudad in enumerate(ciudades):
        plt.annotate(str(i), ciudad)
    # Si se proporciona un título, lo añadimos al gráfico
    if titulo:
        plt.title(titulo)
    # Mostramos el gráfico en pantalla
    plt.show()





# Ejemplo de uso
ciudades = [(60, 200), (180, 200), (80, 180), (140, 180), (20, 160), (100, 160), (200, 160), (140, 140), (40, 120), (100, 120), (180, 100), (60, 80), (120, 80), (180, 60), (20, 40), (100, 40), (200, 40), (20, 20), (60, 20), (160, 20)]
ciudad_inicio = 5  # Índice de la ciudad de inicio
temperatura_inicial = 1000
temperatura_final = 1
factor_enfriamiento = 0.9999
num_iteraciones = 100000



x = [ciudad[0] for ciudad in ciudades]
y = [ciudad[1] for ciudad in ciudades]

# Traza los círculos para las ciudades
plt.plot(x, y, 'co')

# Agrega un número a cada círculo que representa la posición de la ciudad
for i, ciudad in enumerate(ciudades):
    plt.text(ciudad[0], ciudad[1], str(i), ha='center', va='center')

# Muestra el gráfico
plt.show()


ruta_optima, distancia_optima = recocido_simulado(ciudades, temperatura_inicial,  temperatura_final, factor_enfriamiento, num_iteraciones, ciudad_inicio)

print("Ciudad de inicio:", ciudad_inicio)
print("Temperatura inicial:", temperatura_inicial)
print("Factor de enfriamiento:", factor_enfriamiento)
print("Número de iteraciones:", num_iteraciones)
print("Distancia óptima:", distancia_optima)
print("Ruta óptima:", ruta_optima)

# Visualización de las ciudades y la ruta óptima
x = [ciudad[0] for ciudad in ciudades]
y = [ciudad[1] for ciudad in ciudades]
plt.scatter(x, y, color='red')

# Colocar etiquetas en cada ciudad con su número correspondiente
for i, ciudad in enumerate(ciudades):
    # Agregar una etiqueta con el número de la ciudad en la posición ligeramente desplazada
    # en x y en y, para que no se solapen con el punto de la ciudad
    plt.annotate(str(i), (ciudad[0]+1, ciudad[1]+1), fontsize=12, color='green')

# Dibujar cada tramo de la ruta óptima como una línea azul
for i in range(len(ruta_optima)-1):
    plt.plot([ciudades[ruta_optima[i]][0], ciudades[ruta_optima[i+1]][0]], [ciudades[ruta_optima[i]][1], ciudades[ruta_optima[i+1]][1]], color='blue')

# Dibujar el último tramo que une el final de la ruta con el inicio
plt.plot([ciudades[ruta_optima[-1]][0], ciudades[ruta_optima[0]][0]], [ciudades[ruta_optima[-1]][1], ciudades[ruta_optima[0]][1]], color='blue')

# Colocar un punto verde en la ciudad de inicio
plt.scatter(ciudades[ciudad_inicio][0], ciudades[ciudad_inicio][1], color='green')

# Agregar un título con la distancia de la ruta óptima
plt.title(f"Ruta óptima (distancia={distancia_optima})")

# Mostrar el gráfico
plt.show()


#----------------------------------------- teoria-------------------------------
"""

La búsqueda de Temple Simulado es una técnica de optimización que se utiliza para encontrar la solución más óptima de un problema. 
Es un algoritmo metaheurístico que se basa en la simulación de un proceso físico, en el cual se calienta y se enfría un material 
hasta que alcanza una configuración deseada.

El algoritmo de Temple Simulado comienza con una solución inicial y evalúa su calidad utilizando una función de costo.
Luego, se genera una solución vecina modificando la solución actual y se evalúa su calidad. Si la nueva solución es mejor que la solución actual,
se acepta como la nueva solución actual.
Si la nueva solución es peor que la solución actual, se acepta con una probabilidad determinada por una función de enfriamiento y una temperatura actual.
La temperatura disminuye gradualmente durante la búsqueda, lo que permite que el algoritmo escape de óptimos locales.

El proceso de enfriamiento se utiliza para controlar la aceptación de soluciones peores a medida que el algoritmo converge a una solución óptima. 
A medida que la temperatura disminuye, la probabilidad de aceptar soluciones peores también disminuye. La función de enfriamiento es una función 
que determina la tasa de enfriamiento y la temperatura inicial.

El algoritmo de Temple Simulado es un algoritmo iterativo que se ejecuta hasta que se alcanza un número máximo de iteraciones o hasta que
se alcanza un valor de costo deseado. La solución óptima encontrada es la mejor solución encontrada durante el proceso de búsqueda.

El algoritmo de Temple Simulado es utilizado en una amplia gama de problemas de optimización, incluyendo la optimización de rutas, 
la programación de tareas y la optimización de parámetros en modelos matemáticos
"""
