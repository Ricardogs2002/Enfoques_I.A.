import math

def ganador(tablero, jugador):
    # Comprueba si el jugador ha ganado en cualquier fila, columna o diagonal
    return ((tablero[0] == jugador and tablero[1] == jugador and tablero[2] == jugador) or
            (tablero[3] == jugador and tablero[4] == jugador and tablero[5] == jugador) or
            (tablero[6] == jugador and tablero[7] == jugador and tablero[8] == jugador) or
            (tablero[0] == jugador and tablero[3] == jugador and tablero[6] == jugador) or
            (tablero[1] == jugador and tablero[4] == jugador and tablero[7] == jugador) or
            (tablero[2] == jugador and tablero[5] == jugador and tablero[8] == jugador) or
            (tablero[0] == jugador and tablero[4] == jugador and tablero[8] == jugador) or
            (tablero[2] == jugador and tablero[4] == jugador and tablero[6] == jugador))

def fin_juego(tablero):
    # Comprueba si el juego ha terminado
    return ganador(tablero, 'X') or ganador(tablero, 'O') or len(celdas_vacias(tablero)) == 0

def celdas_vacias(tablero):
    # Encuentra las celdas vacías del tablero
    return [i for i, x in enumerate(tablero) if x == '-']

def minimax(tablero, profundidad, alfa, beta, es_maximizador):
    if ganador(tablero, 'X'):
        # Si el jugador X gana, retorna -1 (puntuación mínima)
        return (-1, None)
    elif ganador(tablero, 'O'):
        # Si el jugador O gana, retorna 1 (puntuación máxima)
        return (1, None)
    elif len(celdas_vacias(tablero)) == 0:
        # Si no hay más celdas vacías, el juego termina en empate y retorna 0
        return (0, None)

    if es_maximizador:
        valor = -math.inf # Inicializa el valor como el menor número posible para buscar el mayor
        movimiento = None # Inicializa el movimiento como None
        for celda in celdas_vacias(tablero): # Recorre todas las celdas vacías del tablero
            nuevo_tablero = tablero.copy() # Crea una copia del tablero para realizar una nueva jugada
            nuevo_tablero[celda] = 'O' # Realiza la jugada del jugador O en la celda vacía
            # Llamada recursiva a la función minimax, alternando entre maximizadores y minimizadores
            # Se busca obtener el valor máximo posible para el jugador O, por lo que se llama a minimax con es_maximizador=False
            nuevo_valor = minimax(nuevo_tablero, profundidad + 1, alfa, beta, False)[0]
            if nuevo_valor > valor:
                valor = nuevo_valor # Actualiza el valor con el nuevo valor obtenido, si es mayor que el actual
                movimiento = celda # Actualiza el movimiento con la celda en la que se realizó la jugada
            alfa = max(alfa, valor) # Actualiza el valor de alfa con el valor máximo entre alfa y valor
            if alfa >= beta: # Si alfa es mayor o igual a beta, no hace falta evaluar los otros nodos y se corta la búsqueda
                break
        return (valor, movimiento) # Retorna el valor y el movimiento obtenido para el jugador O
    
    else: # Si no es maximizador
        valor = math.inf # Inicializa el valor como el mayor número posible para buscar el menor
        movimiento = None # Inicializa el movimiento como None
        for celda in celdas_vacias(tablero): # Recorre todas las celdas vacías del tablero
            nuevo_tablero = tablero.copy() # Crea una copia del tablero para realizar una nueva jugada
            nuevo_tablero[celda] = 'X' # Realiza la jugada del jugador X en la celda vacía
            # Llamada recursiva a la función minimax, alternando entre maximizadores y minimizadores
            # Se busca obtener el valor mínimo posible para el jugador X, por lo que se llama a minimax con es_maximizador=True
            nuevo_valor = minimax(nuevo_tablero, profundidad + 1, alfa, beta, True)[0]
            if nuevo_valor < valor:
                valor = nuevo_valor # Actualiza el valor con el nuevo valor obtenido, si es menor que el actual
                movimiento = celda # Actualiza el movimiento con la celda en la que se realizó la jugada
            beta = min(beta, valor) # Actualiza el valor de beta con el valor mínimo entre beta y valor
            if alfa >= beta: # Si alfa es mayor o igual a beta, no hace falta evaluar los otros nodos y se corta la búsqueda
                break
    return (valor, movimiento) # Retorna el valor y el movimiento obtenido para el jugador X


def mejor_movimiento(tablero): #Funcion del movimiento de la Computadora
    return minimax(tablero, 0, -math.inf, math.inf, True)[1] #Llama a la funcion minimax

if __name__ == '__main__':    #Se guarda el tablero vacio
    tablero = ['-', '-', '-',
               '-', '-', '-',
               '-', '-', '-']

    while not fin_juego(tablero): #Mientras el juego no haya terminado
        print("Tablero Actual:") #Dibuja el tablero
        print(tablero[0] + '|' + tablero[1] + '|' + tablero[2])
        print(tablero[3] + '|' + tablero[4] + '|' + tablero[5])
        print(tablero[6] + '|' + tablero[7] + '|' + tablero[8])

        mov_jugador = int(input("Seleccione una posición para hacer su jugada (0-8): "))#Se pide una posicion para mover
        while tablero[mov_jugador] != '-': #Si en la posicion escogina no esta vacia entonces marca error
            print("Movimiento inválido. Por favor, elige una celda vacía.")#Se hace saber el error
            mov_jugador = int(input("Seleccione una posición para hacer su jugada (0-8): "))# Se vuelve a preguntar por una posicion
        tablero[mov_jugador] = 'X'#Se coloca su marca en la posicion

        if not fin_juego(tablero):#Si no es el fin
            print("La computadora está haciendo su jugada...")#Se muestra que la computadora esta pensando
            mov_pc = mejor_movimiento(tablero)#Se llama a la funcion de la computadora
            tablero[mov_pc] = 'O'# Se pone la marca en la mejor posicion

    print("Tablero Final:") #Se imprime el tablero final
    print(tablero[0] + '|' + tablero[1] + '|' + tablero[2])
    print(tablero[3] + '|' + tablero[4] + '|' + tablero[5])
    print(tablero[6] + '|' + tablero[7] + '|' + tablero[8])

    if ganador(tablero, 'X'):   #Se muestran resultados
        print("¡Ganaste! :)")
    elif ganador(tablero, 'O'):
        print("¡Perdiste! :(")
    else:
        print("¡Empate!") 
