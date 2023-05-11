"""La búsqueda de minimax esperado es una variante del algoritmo minimax que
se utiliza en juegos con incertidumbre, como el póker, en los que no se conoce
completamente el estado del juego. En este tipo de juegos, se utiliza la
probabilidad para calcular el valor de un nodo.

En lugar de asignar valores fijos a los nodos hoja como en el algoritmo
minimax, el minimax esperado asigna valores esperados basados en las
probabilidades de que ocurran ciertos eventos. Para calcular estos valores, se
utiliza la teoría de la probabilidad, y se aplican los mismos principios de
minimización y maximización que en el algoritmo minimax."""


import random

def get_user_input():
    """Pide al usuario que introduzca el número que desea adivinar."""
    user_input = input("Introduce el número que deseas adivinar: ")
    while not user_input.isdigit():
        user_input = input("Introduce un número válido: ")
    return int(user_input)

def get_computer_guess(min_val, max_val, prob):
    """Utiliza el algoritmo minimax esperado para adivinar el número."""
    guess = (min_val + max_val) // 2  # Adivina el número medio del rango
    if random.random() < prob:  # Si el número es menor que la probabilidad
        guess += 1  # Incrementa el número para explorar un posible siguiente valor
    return guess

def main():
    """Función principal del programa."""
    print("¡Bienvenido al juego de adivinanza de números!")
    min_val = 1
    max_val = 100
    prob = 0.5
    num_guesses = 0
    target_num = get_user_input()

    while True:
        num_guesses += 1
        guess = get_computer_guess(min_val, max_val, prob)
        print(f"¿Es {guess} el número que deseas adivinar?")

        if guess == target_num:
            print(f"¡Correcto! El número era {guess}.")
            print(f"Has necesitado {num_guesses} intentos.")
            break
        elif guess > target_num:
            print("No, es demasiado alto.")
            max_val = guess - 1  # Ajusta el rango para explorar números más bajos
        else:
            print("No, es demasiado bajo.")
            min_val = guess + 1  # Ajusta el rango para explorar números más altos

if __name__ == "__main__":
    main()
