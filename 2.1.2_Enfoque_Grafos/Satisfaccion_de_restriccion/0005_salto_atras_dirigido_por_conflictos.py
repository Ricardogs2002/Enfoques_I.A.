
import numpy as np
from collections import Counter



class Ntorres:

    def __init__(self, tamaño_del_tablero):
        self.tamaño = tamaño_del_tablero
        self.columna = [] * self.tamaño
        self.num_de_casillas = 0
        self.num_de_retrocesos = 0
        self.conflict_set = {}
        for i in range(self.tamaño):
            self.conflict_set[i] = []


    def casillas(self, fila_inicial=0):
        """ Algoritmo de retroceso para colocar torres recursivamente en el tablero
            argumentos:
                fila_inicial: la fila en la que se intenta comenzar a colocar la torre
            devoluciones:
                lista que representa una solucion
        """
        # si cada columna tiene una torre, tenemos una solución

        if len(self.columna) == self.tamaño:
            print('¡Solución encontrada! El tamaño del tablero fue:' + str(self.tamaño))
            print(str(self.num_de_casillas) + ' casillas fueron hechos en total')
            print(str(self.num_de_retrocesos) + ' retrocesos totales se ejecutaron')
            print(self.columna)
            return self.columna

        # de lo contrario, busca una ubicación segura para la torre
        else:
            for fila in range(fila_inicial, self.tamaño):
               # si existe una ubicación segura en esta columna
              
                if self.Casilla_Segura(len(self.columna), fila) is True:
                    # coloca una torre en la ubicación
                    self.columna.insert(len(self.columna),fila)
                    self.num_de_casillas += 1
                    # llama recursivamente a casillas() en la siguiente columna
                    return self.casillas()

                # si no es posible, vuelve al último estado y trata de colocar la torre
            else:
                # obtiene la última fila desde donde hacer el retroceso
                ultimafila = self.conflict_set[len(self.columna)]
                self.num_de_retrocesos += 1
                temp = Counter(ultimafila)
                ultimafila = max(temp,key=temp.get)
                # inicializa la variable a valor inicial
                self.conflict_set[len(self.columna)] = []
                pervious_variable = self.columna.pop(ultimafila)
                # llama recursivamente a casillas() desde la última posición conocida buena, incrementando a la siguiente fila
                return self.casillas(fila_inicial = pervious_variable)

    def Casilla_Segura(self, col, fila):
        """Determina si un movimiento es legal.
        argumentos:
            col: columna de la ubicación deseada
            fila: fila de la ubicación deseada
            self.columna: lista de torres presentes en el tablero
        devoluciones:
            True si es seguro, False en caso contrario
        """
        # verifica las amenazas de cada torre actualmente en el tablero
        for amenzaFila in self.columna:
            amenzacolum = self.columna.index(amenzaFila)
            # verifica las amenazas horizontales/verticales
            if fila == amenzaFila or col == self.columna.index(amenzaFila):
                self.conflict_set [col].append(amenzacolum)
                return False
            # acomodamos las torres de manera no tipica en base las diagonales
            elif amenzaFila + amenzacolum == fila + col or amenzaFila - amenzacolum == fila - col:
                self.conflict_set[col].append(amenzacolum)
                return False
        # si llegamos aquí, no hay amenazas presentes y es seguro colocar la torre en la (columna, fila)
        return True

# verifica las amenazas
tamaño = input("Introduce el tamaño del tablero:")
n = int(tamaño)
# crear una instancia del tablero y llamar al algoritmo de retroceso
torres = Ntorres(n)
torres.casillas()
# convertir el tablero en una matriz numpy para una impresión
tablero = np.array([["0"] * n] * n)
for torre in torres.columna:
    tablero[torres.columna.index(torre), torre] = 'T'

print(tablero.T)
