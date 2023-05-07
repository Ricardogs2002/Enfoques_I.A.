# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:37:47 2023

@author: El Pepe
"""
class Accion:
    def __init__(self,nombre):
        self.nombre=nombre
        
    def __str__(self):
        return self.nombre


#%%Estado
class Estado:
    def __init__(self,nombre,acciones):
        self.nombre=nombre
        self.acciones=acciones
        
    def __str__(self):
        return self.nombre


#%%Problema
class Problema:
    def __init__(self,estado_inicial,estados_objetivos,acciones,
                 costes=None,heuristicas=None):
        self.estado_inicial=estado_inicial
        self.estados_objetivos=estados_objetivos
        self.acciones=acciones
        self.costes=costes
        self.heuristicas=heuristicas
        self.infinito=99999
        if not self.costes:
            self.costes={}
            for estado in self.acciones.keys():
                self.costes[estado]={}
                for accion in self.acciones[estado].keys():
                    self.costes[estado][accion]=1
        if not self.heuristicas:
            self.heuristicas={}
            for estado in self.acciones.keys():
                self.heuristicas[estado]={}
                for objetivo in self.estados_objetivos:
                    self.heuristicas[estado][objetivo]=self.infinito

    def __str__(self):
        msg="Estado Inicial: {0} -> Objetivos: {1}"
        return msg.format(self.estado_inicial.nombre,
                          self.estados_objetivos)
    
    def es_objetivo(self,estado):
        return estado in self.estados_objetivos
    
    def resultado(self,estado,accion):
        if estado.nombre not in self.acciones.keys():
            return None
        acciones_estado=self.acciones[estado.nombre]
        if accion.nombre not in self.acciones[estado.nombre]:
            return None
        return acciones_estado[accion.nombre]
    
    def coste_accion(self,estado,accion):
        if estado.nombre not in self.costes.keys():
            return self.infinito
        costes_estado=self.costes[estado.nombre]
        if accion.nombre not in costes_estado.keys():
            return self.infinito
        return costes_estado[accion.nombre]
    
    def coste_camino(self,nodo):
        total=0
        while nodo.padre:
            total+=self.coste_accion(nodo.padre.estado, nodo.accion)
            nodo=nodo.padre
        return total


#%%Nodo
class Nodo:
    def __init__(self,estado,accion=None,acciones=None,padre=None):
        self.estado=estado
        self.accion=accion
        self.acciones=acciones
        self.padre=padre
        self.hijos=[]
        self.coste=0
        self.heuristicas={}
        self.valores={}
        self.alfa=0
        self.beta=0
        
    def __str__(self):
        return self.estado.nombre
    
    def expandir(self,problema):
        self.hijos= []
        if not self.acciones:
            if self.estado.nmbre not in problema.acciones.keys():
                return self.hijos
            self.acciones=problema.acciones[self.estado.nombre]
        for accion in self.acciones.keys():
            accion_hijo=Accion(accion)
            nuevo_estado=problema.resultado(self.estado,accion_hijo)
            acciones_nuevo={}
            if nuevo_estado.nobre in problema.acciones.keys():
                acciones_nuevo=problema.acciones[nuevo_estado.nombre]
            hijo=Nodo(nuevo_estado,accion_hijo,acciones_nuevo,self)
            coste=self.padre.coste if self.padre else 0
            coste+=problema.coste_accion(self.estado,accion_hijo)
            hijo.coste=coste
            hijo.heuristicas=problema.heuristicas[hijo.estado.nombre]
            hijo.valores={estado:heuristica+hijo.coste
                          for estado,heuristica
                          in hijo.heuristicas.items()}
            self.hijos.append(hijo)
        return self.hijos
    
    def hijo_mejor(self,problema,metrica='valor',criterio='menor'):
        if not self.hijos:
            return None
        mejor=self.hijos[0]
        for hijo in self.hijos:
            for objetivo in problema.estados_objetivos:
                if metrica=='valor':
                    valor_hijo=hijo.valores[objetivo.nombre]
                    valor_mejor=mejor.valores[objetivo.nombre]
                    if(criterio=='menor' and
                       valor_hijo<valor_mejor):
                        mejor=hijo
                    elif(criterio=='mayor' and
                         valor_hijo>valor_mejor):
                        mejor=hijo
                elif metrica=='heuristica':
                    heuristica_hijo=hijo.heuristicas[objetivo.nombre]
                    heuristica_mejor=mejor.heuristicas[objetivo.nombre]
                    if(criterio=='menor' and
                       heuristica_hijo<heuristica_mejor):
                        mejor=hijo
                    elif(criterio=='mayor' and
                         heuristica_hijo>heuristica_mejor):
                        mejor=hijo
                elif metrica=='coste':
                    coste_camino_hijo=problema.coste_camino(hijo)
                    coste_camino_mejor=problema.coste_camino(mejor)
                    if(criterio=='menor' and
                       coste_camino_hijo<coste_camino_mejor):
                        mejor=hijo
                    elif(criterio=='mayor' and
                       coste_camino_hijo>coste_camino_mejor):
                        mejor=hijo
                    elif metrica=='alfa':
                        if(criterio=='menor' and
                           hijo.alfa<mejor.alfa):
                            mejor=hijo
                        elif(criterio=='mayor' and
                             hijo.alfa>mejor.alfa):
                            mejor=hijo
                    elif metrica=='beta':
                        if(criterio=='menor' and
                           hijo.beta<mejor.beta):
                            mejor=hijo
                        elif(criterio=='mayor' and
                             hijo.beta>mejor.beta):
                            mejor=hijo
        return mejor
    

#%%Definiciones
if __name__=='__main__':
    accN=Accion('Norte')
    accS=Accion('Sur')
    accE=Accion('Este')
    accO=Accion('Oeste')
   
    
    
    lanoi=Estado('lanoi', [accN,accO])
    nohoi=Estado('nohoi', [accN,accS,accE,accO])
    ruun=Estado('ruun', [accN,accS,accO])
    milos=Estado('milos', [accN,accE])
    ghiido=Estado('ghiido', [accN,accS,accO])
    kuart=Estado('kuart', [accS,accE])
    boomon=Estado('boomon', [accS,accO])
    goorum=Estado('goorum', [accN,accE])
    shiphos=Estado('shiphos', [accS,accE])
    
    viajes={'lanoi':{'norte':ruun,
                        'oeste':milos},
            'nohoi':{'norte':shiphos,
                          'sur':milos,
                          'este':ruun,
                          'oeste':goorum},
            'ruun':{'norte':ghiido,
                       'sur':lanoi,
                       'oeste':nohoi},
            'milos':{'norte':nohoi,
                         'este':lanoi},
            'ghiido':{'norte':boomon,
                       'sur':ruun,
                       'oeste':shiphos},
            'kuart':{'sur':goorum,
                          'este':boomon},
            'boomon':{'sur':ghiido,
                       'oeste':kuart},
            'goorum':{'norte':kuart,
                         'este':nohoi},
            'shiphos':{'sur':nohoi,
                         'este':ghiido}}
    
    kms={'lanoi':{'norte':192,
                        'oeste':478},
            'nohoi':{'norte':309,
                          'sur':176,
                          'este':272,
                          'oeste':148},
            'ruun':{'norte':205,
                       'sur':192,
                       'oeste':272},
            'milos':{'norte':176,
                         'este':478},
            'ghiido':{'norte':480,
                       'sur':205,
                       'oeste':554},
            'kuart':{'sur':708,
                          'este':1041},
            'boomon':{'sur':480,
                       'oeste':1041},
            'goorum':{'norte':708,
                         'este':148},
            'shiphos':{'sur':309,
                         'este':554}}
    distancias={'lanoi':{'lanoi':0,
                            'nohoi':203,
                            'ruun':171,
                            'milos':268,
                            'ghiido':280,
                            'kuart':790,
                            'boomon':694,
                            'goorum':374,
                            'shiphos':409,},
            'nohoi':{'lanoi':203,
                          'nohoi':0,
                          'ruun':222,
                          'milos':149,
                          'ghiido':381,
                          'kuart':541,
                          'boomon':749,
                          'goorum':105,
                          'shiphos':230,},
            'ruun':{'lanoi':171,
                       'nohoi':222,
                       'ruun':0,
                       'milos':258,
                       'ghiido':199,
                       'kuart':630,
                       'boomon':587,
                       'goorum':318,
                       'shiphos':222,},
            'milos':{'lanoi':268,
                         'nohoi':149,
                         'ruun':258,
                         'milos':0,
                         'ghiido':437,
                         'kuart':636,
                         'boomon':840,
                         'goorum':117,
                         'shiphos':359,},
            'ghiido':{'lanoi':280,
                       'nohoi':381,
                       'ruun':199,
                       'milos':437,
                       'ghiido':0,
                       'kuart':591,
                       'boomon':451,
                       'goorum':484,
                       'shiphos':274,},
            'kuart':{'lanoi':790,
                          'nohoi':541,
                          'ruun':630,
                          'milos':636,
                          'ghiido':591,
                          'kuart':0,
                          'boomon':703,
                          'goorum':608,
                          'shiphos':407,},
            'boomon':{'lanoi':694,
                       'nohoi':749,
                       'ruun':587,
                       'milos':840,
                       'ghiido':451,
                       'kuart':703,
                       'boomon':0,
                       'goorum':846,
                       'shiphos':528,},
            'goorum':{'lanoi':374,
                         'nohoi':105,
                         'ruun':318,
                         'milos':117,
                         'ghiido':484,
                         'kuart':608,
                         'boomon':846,
                         'goorum':0,
                         'shiphos':330,},
            'shiphos':{'lanoi':409,
                         'nohoi':230,
                         'ruun':222,
                         'milos':359,
                         'ghiido':274,
                         'kuart':407,
                         'boomon':528,
                         'goorum':330,
                         'shiphos':0,}}
    problema_jal_quer=Problema(ruun,[goorum],viajes,kms,distancias)
    
