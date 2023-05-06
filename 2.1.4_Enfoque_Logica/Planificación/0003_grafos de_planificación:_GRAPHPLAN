#< -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 08:09:59 2023
@author: 6E1
"""

import numpy as np

class GraphPlan:
    def __init__(self, acciones, estado_inicial, estado_objetivo):
        self.acciones = acciones
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo

        # Preprocesamiento
        self.atoms = np.concatenate((estado_inicial, estado_objetivo))
        self.capa_acciones = self.crear_capa_acciones()
        self.capa_hechos = self.crear_capa_hechos()

    def crear_capa_acciones(self):
        capa_acciones = []
        for i, accion in enumerate(self.acciones):
            precondiciones = accion[0]
            efectos = accion[1]
            capa_accion = {'id': i, 'pre': precondiciones, 'efc': efectos}
            capa_acciones.append(capa_accion)
        return capa_acciones

    def crear_capa_hechos(self):
        capa_hechos = []
        for i, atom in enumerate(self.atoms):
            capa_hecho = {'id': i, 'atom': atom}
            capa_hechos.append(capa_hecho)
        return capa_hechos

    def graphplan(self):
        capas = [self.estado_inicial]

        # Expansión
        while True:
            capa_previa = capas[-1]
            nueva_capa = []
            for accion in self.capa_acciones:
                # Comprobamos si se satisfacen las precondiciones de la accion
                if all([pre in capa_previa for pre in accion['pre']]):
                    # Añadimos los efectos de la accion a la nueva capa
                    for efc in accion['efc']:
                        if efc not in nueva_capa:
                            nueva_capa.append(efc)

            # Comprobamos si la nueva capa es igual a la anterior
            if nueva_capa == capa_previa:
                return None

            # Comprobamos si se ha alcanzado el objetivo
            if all([goal in nueva_capa for goal in self.estado_objetivo]):
                capas.append(self.estado_objetivo)
                return capas

            capas.append(nueva_capa)

        # Retroceso
        while True:
            capa_previa = capas[-1]
            nueva_capa = []
            for fact in self.capa_hechos:
                # Comprobamos si el hecho no está en la capa anterior
                if fact['atom'] not in capa_previa:
                    # Comprobamos si hay una accion que tenga el efecto como precondición
                    action_ids = [accion['id'] for accion in self.capa_acciones if fact['atom'] in accion['efc']]
                    # Comprobamos si todas las precondiciones de los actions se satisfacen
                    if all([all([pre in capa_previa for pre in self.capa_acciones[action_id]['pre']]) for action_id in action_ids]):
                        nueva_capa.append(fact['atom'])

            # Comprobamos si la nueva capa es igual a la anterior
            if nueva_capa == capa_previa:
                return None

            # Comprobamos si se ha alcanzado el objetivo
            if all([goal in nueva_capa for goal in self.estado_objetivo]):
                capas.append(self.estado_objetivo)
                return capas

            capas.append(nueva_capa)
# Definimos las acciones
acciones = [
    (['At', 'S1'], ['At', 'S2']),
    (['At', 'S2'], ['At', 'S1']),
    (['At', 'S1'], ['Has', 'C1']),
    (['Has', 'C1'], ['At', 'S1']),
    (['Has', 'C1'], ['Has', 'C2']),
    (['Has', 'C2'], ['Has', 'C1']),
    (['At', 'S2'], ['Has', 'C3']),
    (['Has', 'C3'], ['At', 'S2']),
]

# Definimos el estado inicial y el estado objetivo
estado_inicial = ['At', 'S1']
estado_objetivo = ['Has', 'C2']

# Creamos el objeto GraphPlan
gp = GraphPlan(acciones, estado_inicial, estado_objetivo)

# Ejecutamos el algoritmo GraphPlan
plan = gp.graphplan()

# Imprimimos el plan
if plan is not None:
    print("Plan encontrado:")
    for i, capa in enumerate(plan):
        print(f"Capa {i}: {capa}")
else:
    print("No se encontró un plan.")
