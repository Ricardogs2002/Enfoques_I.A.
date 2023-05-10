import random  # Importa la biblioteca random para generar números aleatorios

while True:  # Inicia un bucle infinito
    aleatorio = random.randrange(0, 3)  # Genera un número aleatorio entre 0 y 2
    eligePc = ""  # Inicializa la elección de la PC como una cadena vacía
    print("1)Piedra")  # Imprime las opciones del usuario
    print("2)Papel")
    print("3)Tijera")
    opcion = int(input("Que eliges (0 para salir): "))  # Espera la elección del usuario y la convierte en entero
    
    if opcion == 0:  # Si el usuario elige 0, sale del bucle
        print("Gracias por jugar!")
        break
    
    # Si el usuario elige 1, 2 o 3, asigna su elección a una cadena
    if opcion == 1:
        eligeUsuario = "piedra"
    elif opcion == 2:
        eligeUsuario = "papel"
    elif opcion == 3:
        eligeUsuario = "tijera"
    else:  # Si el usuario ingresa un valor inválido, continúa con la siguiente iteración del bucle
        print("Opción inválida. Intenta de nuevo.")
        continue
    
    print("Tu eliges: ", eligeUsuario)  # Imprime la elección del usuario
    
    # Asigna la elección de la PC en función del número aleatorio generado
    if aleatorio == 0:
        eligePc = "piedra"
    elif aleatorio == 1:
        eligePc = "papel"
    elif aleatorio == 2:
        eligePc = "tijera"
    print("PC eligió: ", eligePc)  # Imprime la elección de la PC
    
    print("...")  # Imprime puntos suspensivos para indicar que el juego está en curso
    
    # Comprueba quién ganó y muestra el resultado
    if eligePc == "piedra" and eligeUsuario == "papel":
        print("Ganaste, papel envuelve piedra")
    elif eligePc == "papel" and eligeUsuario == "tijera":
        print("Ganaste, Tijera corta papel")
    elif eligePc == "tijera" and eligeUsuario == "piedra":
        print("Ganaste, Piedra pisa tijera")
    elif eligePc == "papel" and eligeUsuario == "piedra":
        print("perdiste, papel envuelve piedra")
    elif eligePc == "tijera" and eligeUsuario == "papel":
        print("perdiste, Tijera corta papel")
    elif eligePc == "piedra" and eligeUsuario == "tijera":
        print("perdiste, Piedra pisa tijera")
    elif eligePc == eligeUsuario:
        print("empate")  # Si ambos eligen lo mismo, muestra un empate


""" 
La teoría de juegos es una herramienta
muy útil para la inteligencia artificial, 
ya que permite modelar situaciones en las que varios
agentes interactúan entre sí y toman decisiones que 
afectan el resultado final de la interacción. La teoría de 
juegos es una rama de las matemáticas y la economía 
que estudia la toma de decisiones en situaciones de conflicto o c
ompetencia entre diferentes actores.
"""
