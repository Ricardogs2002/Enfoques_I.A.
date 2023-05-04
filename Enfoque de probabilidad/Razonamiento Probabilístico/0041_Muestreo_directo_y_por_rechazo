#Implementación de muestreo directo y por rechazo
import random

# Muestreo Directo usando como ejemplo la suma de dos dados
def direct_sampling(num_samples):
    # Define una función auxiliar que genera la suma de dos dados al azar
    def dice_sum():
        # Genera dos números enteros aleatorios entre 1 y 6 y los suma
        return random.randint(1, 6) + random.randint(1, 6)

    # Inicializa un contador en cero para contar cuántas veces se obtiene una suma de 7
    count = 0
    # Genera num_samples muestras y cuenta cuántas de ellas suman 7
    for i in range(num_samples):
        # Genera una muestra de la suma de dos dados
        if dice_sum() == 7:  # Si la suma es igual a 7
            count += 1  # Incrementa el contador en 1
    # Calcula la probabilidad estimada de obtener una suma de 7 dividiendo el número de muestras que suman 7 entre el número total de muestras
    return count / num_samples


# Muestreo por rechazo usando como ejemplo la suma de dos dados
def rejection_sampling(num_samples):
    # Define una función que simula el lanzamiento de dos dados y devuelve su suma
    def dice_sum():
        # Genera dos muestras aleatorias de números enteros en el rango [1, 6] y devuelve su suma
        return random.randint(1, 6) + random.randint(1, 6)

    # Inicializa un contador en cero para contar cuántas muestras aceptadas se han generado
    count = 0
    # Genera num_samples muestras de la distribución uniforme en el rango [1, 6]
    for i in range(num_samples):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        # Comprueba si la suma de las dos muestras generadas es igual a 7
        if x + y == 7:
            # Si la condición se cumple, incrementa el contador de muestras aceptadas en 1
            count += 1
        else:
            # Si la condición no se cumple, la muestra es rechazada y se continúa con el siguiente ciclo
            continue
    # Devuelve la proporción de muestras aceptadas como una estimación de la probabilidad de que la suma de dos dados sea igual a 7
    return count / num_samples

# Llama a la función direct_sampling() con un argumento de 10000 para generar 10,000 muestras
# y estimar la probabilidad de obtener una suma de 7 al lanzar dos dados
print("Probabilidad estimada de obtener una suma de 7 al lanzar dos dados usando Muestreo Directo: ", direct_sampling(10000))

# Imprime el resultado de la simulación utilizando el método de muestreo por rechazo 
# con un número de muestras igual a 10,000
print("\n\nProbabilidad estimada de obtener una suma de 7 al lanzar dos dados usando Muestreo por Rechazo: ", rejection_sampling(10000))

# Nota: El muestreo directo es más adecuado para distribuciones sencillas y 
# El muestreo por rechazo es más adecuado para distribuciones complejas.
