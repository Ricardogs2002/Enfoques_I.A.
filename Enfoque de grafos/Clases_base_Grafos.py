# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 05:06:59 2023

@author: 6E1
"""


#%%Acción
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
    accN=Accion('norte')
    accS=Accion('sur')
    accE=Accion('este')
    accO=Accion('oeste')
    
    colima=Estado('A Colima', [accN,accO])
    guanajuato=Estado('Guanajuato', [accN,accS,accE,accO])
    jalisco=Estado('Jalisco', [accN,accS,accO])
    michoacan=Estado('Michoacan', [accN,accE])
    nayarit=Estado('Nayarit', [accN,accS,accO])
    nuevoleon=Estado('Nuevo León', [accS,accE])
    sinaloa=Estado('Sinaloa', [accS,accO])
    queretaro=Estado('Querétaro', [accN,accE])
    zacatecas=Estado('Zacatecas', [accS,accE])
    
    viajes={'A Colima':{'norte':jalisco,
                        'oeste':michoacan},
            'Guanajuato':{'norte':zacatecas,
                          'sur':michoacan,
                          'este':jalisco,
                          'oeste':queretaro},
            'Jalisco':{'norte':nayarit,
                       'sur':colima,
                       'oeste':guanajuato},
            'Michoacan':{'norte':guanajuato,
                         'este':colima},
            'Nayarit':{'norte':sinaloa,
                       'sur':jalisco,
                       'oeste':zacatecas},
            'Nuevo León':{'sur':queretaro,
                          'este':sinaloa},
            'Sinaloa':{'sur':nayarit,
                       'oeste':nuevoleon},
            'Querétaro':{'norte':nuevoleon,
                         'este':guanajuato},
            'Zacatecas':{'sur':guanajuato,
                         'este':nayarit}}
    
    kms={'A Colima':{'norte':192,
                        'oeste':478},
            'Guanajuato':{'norte':309,
                          'sur':176,
                          'este':272,
                          'oeste':148},
            'Jalisco':{'norte':205,
                       'sur':192,
                       'oeste':272},
            'Michoacan':{'norte':176,
                         'este':478},
            'Nayarit':{'norte':480,
                       'sur':205,
                       'oeste':554},
            'Nuevo León':{'sur':708,
                          'este':1041},
            'Sinaloa':{'sur':480,
                       'oeste':1041},
            'Querétaro':{'norte':708,
                         'este':148},
            'Zacatecas':{'sur':309,
                         'este':554}}
    distancias={'A Colima':{'A Colima':0,
                            'Guanajuato':203,
                            'Jalisco':171,
                            'Michoacan':268,
                            'Nayarit':280,
                            'Nuevo León':790,
                            'Sinaloa':694,
                            'Querétaro':374,
                            'Zacatecas':409,},
            'Guanajuato':{'A Colima':203,
                          'Guanajuato':0,
                          'Jalisco':222,
                          'Michoacan':149,
                          'Nayarit':381,
                          'Nuevo León':541,
                          'Sinaloa':749,
                          'Querétaro':105,
                          'Zacatecas':230,},
            'Jalisco':{'A Colima':171,
                       'Guanajuato':222,
                       'Jalisco':0,
                       'Michoacan':258,
                       'Nayarit':199,
                       'Nuevo León':630,
                       'Sinaloa':587,
                       'Querétaro':318,
                       'Zacatecas':222,},
            'Michoacan':{'A Colima':268,
                         'Guanajuato':149,
                         'Jalisco':258,
                         'Michoacan':0,
                         'Nayarit':437,
                         'Nuevo León':636,
                         'Sinaloa':840,
                         'Querétaro':117,
                         'Zacatecas':359,},
            'Nayarit':{'A Colima':280,
                       'Guanajuato':381,
                       'Jalisco':199,
                       'Michoacan':437,
                       'Nayarit':0,
                       'Nuevo León':591,
                       'Sinaloa':451,
                       'Querétaro':484,
                       'Zacatecas':274,},
            'Nuevo León':{'A Colima':790,
                          'Guanajuato':541,
                          'Jalisco':630,
                          'Michoacan':636,
                          'Nayarit':591,
                          'Nuevo León':0,
                          'Sinaloa':703,
                          'Querétaro':608,
                          'Zacatecas':407,},
            'Sinaloa':{'A Colima':694,
                       'Guanajuato':749,
                       'Jalisco':587,
                       'Michoacan':840,
                       'Nayarit':451,
                       'Nuevo León':703,
                       'Sinaloa':0,
                       'Querétaro':846,
                       'Zacatecas':528,},
            'Querétaro':{'A Colima':374,
                         'Guanajuato':105,
                         'Jalisco':318,
                         'Michoacan':117,
                         'Nayarit':484,
                         'Nuevo León':608,
                         'Sinaloa':846,
                         'Querétaro':0,
                         'Zacatecas':330,},
            'Zacatecas':{'A Colima':409,
                         'Guanajuato':230,
                         'Jalisco':222,
                         'Michoacan':359,
                         'Nayarit':274,
                         'Nuevo León':407,
                         'Sinaloa':528,
                         'Querétaro':330,
                         'Zacatecas':0,}}
    problema_jal_quer=Problema(jalisco,[queretaro],viajes,kms,distancias)
    
    
