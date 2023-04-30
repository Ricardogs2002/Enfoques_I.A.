import sys
import numpy as np
from collections import Counter
import time


class NReinas:

    def __init__(self, tamaño_del_tablero):
        self.tamaño = tamaño_del_tablero
        self.columna = [] * self.tamaño
        self.num_of_places = 0
        self.num_of_backtracks = 0
        self.conflict_set = {}
        for i in range(self.tamaño):
            self.conflict_set[i] = []


    def place(self, startRow=0):
        """ Algoritmo de retroceso para colocar reinas recursivamente en el tablero
            argumentos:
                startRow: la fila en la que se intenta comenzar a colocar la reina
            devoluciones:
                lista que representa una solucion
        """
        # si cada columna tiene una reina, tenemos una solución

        if len(self.columna) == self.tamaño:
            print('¡Solución encontrada! El tamaño del tablero fue:' + str(self.tamaño))
            print(str(self.num_of_places) + ' lugares fueron hechos en total')
            print(str(self.num_of_backtracks) + ' retrocesos totales se ejecutaron')
            print(self.columna)
            return self.columna

        # de lo contrario, busca una ubicación segura para la reina
        else:
            for row in range(startRow, self.tamaño):
               # si existe una ubicación segura en esta columna


                if self.isSafe(len(self.columna), row) is True:
                    # coloca una reina en la ubicación
                    self.columna.insert(len(self.columna),row)
                    self.num_of_places += 1
                    # llama recursivamente a place() en la siguiente columna
                    return self.place()

                # si no es posible, vuelve al último estado y trata de colocar la reina
            else:
                # obtiene la última fila desde donde hacer el retroceso
                lastRow = self.conflict_set[len(self.columna)]
                self.num_of_backtracks += 1
                temp = Counter(lastRow)
                lastRow = max(temp,key=temp.get)
                # inicializa la variable a valor inicial
                self.conflict_set[len(self.columna)] = []
                pervious_variable = self.columna.pop(lastRow)
                # llama recursivamente a place() desde la última posición conocida buena, incrementando a la siguiente fila
                return self.place(startRow = pervious_variable)

    def isSafe(self, col, row):
        """Determina si un movimiento es legal.
        argumentos:
            col: columna de la ubicación deseada
            fila: fila de la ubicación deseada
            self.columna: lista de reinas presentes en el tablero
        devoluciones:
            True si es seguro, False en caso contrario
        """
        # verifica las amenazas de cada reina actualmente en el tablero
        for threatRow in self.columna:
           # para mayor legibilidad
            threatCol = self.columna.index(threatRow)
            # verifica las amenazas horizontales/verticales
            if row == threatRow or col == self.columna.index(threatRow):
                self.conflict_set [col].append(threatCol)
                return False
            # check for diagonal threats
            elif threatRow + threatCol == row + col or threatRow - threatCol == row - col:
                self.conflict_set[col].append(threatCol)
                return False
        # si llegamos aquí, no hay amenazas presentes y es seguro colocar la reina en la (columna, fila)
        return True

# verifica las amenazas
tamaño = input("Introduce el tamaño del tablero:")
n = int(tamaño)
# crear una instancia del tablero y llamar al algoritmo de retroceso
start = time.time()
queens = NReinas(n)
queens.place(0)
stop = time.time()
seconds = stop - start
print("Tiempo requerido para la ejecución",seconds*1000)
# convertir el tablero en una matriz numpy para una impresión bonita
board = np.array([[' '] * n] * n)
for queen in queens.columna:
    board[queens.columna.index(queen), queen] = 'Q'

print(board.T)
