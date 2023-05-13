
# Lógicas de Orden Superior

import random

# Definimos una función que toma como argumento otra función
def aplicar_operacion(num, func):
    # Generamos un número aleatorio
    aleatorio = random.randint(1, 10)
    # Devolvemos el resultado de aplicar la función al número aleatorio
    resultado = func(num, aleatorio)
    # Imprimimos el número aleatorio generado junto con el resultado de la función
    print(f"Número aleatorio generado: {aleatorio}")
    return resultado

# Definimos algunas funciones para usar como argumento en aplicar_operacion
def multiplicar(x, y):
    return x * y

def sumar(x, y):
    return x + y

def cuadrado(x, y):
    return x ** y


# Ejemplo de uso de la función aplicar_operacion con las funciones duplicar y cuadrado
print(aplicar_operacion(5, multiplicar))  # Salida: Un número aleatorio entre 5 y 50
print(aplicar_operacion(5, sumar))  # Salida: un número aleatorio entre 6 y 15
print(aplicar_operacion(5, cuadrado))  # Salida: 5 elevado a un número aleatorio entre 1 y 10
