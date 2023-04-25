# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:27:54 2023
@author: 6E1
"""

from Grafos import Accion
from Grafos import Estado
from Grafos import Nodo
from Grafos import Problema

#%%
def anchura(problema):
    raiz=crea_nodo_raiz(problema)
    if problema.es_objetivo(raiz.estado):
        return raiz
    frontera=[raiz,]
    explorados=set()
    while True:
        print("frontera: ",[nodo.estado.nombre for nodo in frontera])
        print("explorados: ",[estado.nombre for estado in explorados])
        if not frontera:
            return None
        nodo=frontera.pop(0)
        print("escoge: ",nodo.estado.nombre)
        print("-------")
        explorados.add(nodo.estado)
        if not nodo.acciones:
            continue
        for nombre_accion in nodo.acciones.keys():
            accion=Accion(nombre_accion)
            hijo=crea_nodo_hijo(problema,nodo,accion)
            estados_frontera=[nodo.estado for nodo in frontera]
            if(hijo.estado not in explorados and
               hijo.estado not in estados_frontera):
                if problema.es_objetivo(hijo.estado):
                    return hijo
                frontera.append(hijo)
                
#%%
def crea_nodo_raiz(problema):
    estado_raiz=problema.estado_inicial
    acciones_raiz={}
    if estado_raiz.nombre in problema.acciones.keys():
        acciones_raiz=problema.acciones[estado_raiz.nombre]
    raiz=Nodo(estado_raiz,None,acciones_raiz,None)
    return raiz

#%%
def crea_nodo_hijo(problema,padre,accion):
    nuevo_estado=problema.resultado(padre.estado,accion)
    acciones_nuevo={}
    if nuevo_estado.nombre in problema.acciones.keys():
        acciones_nuevo=problema.acciones[nuevo_estado.nombre]
        hijo=Nodo(nuevo_estado,accion,acciones_nuevo,padre)
        padre.hijos.append(hijo)
        return hijo
    
#%%
def muestra_solucion(objetivo=None):
    if not objetivo:
        print("no hay solución")
        return
    nodo=objetivo
    while nodo:
        msg="Estado: {0}"
        print(msg.format(nodo.estado.nombre))
        if nodo.accion:
            msg="<--- {0} ---"
            print(msg.format(nodo.accion.nombre))
        nodo=nodo.padre
            

#%%Definiciones
if __name__=='__main__':
    accN=Accion('N')
    accS=Accion('S')
    accE=Accion('E')
    accO=Accion('O')
    accNE=Accion('NE')
    accNO=Accion('NO')
    accSE=Accion('SE')
    accSO=Accion('SO')
    
    colima=Estado('Colima', [accN,accO])
    guanajuato=Estado('Guanajuato', [accN,accS,accE,accO])
    jalisco=Estado('Jalisco', [accN,accS,accO])
    michoacan=Estado('Michoacan', [accN,accE])
    nayarit=Estado('Nayarit', [accN,accS,accO])
    nuevoleon=Estado('Nuevo León', [accS,accE])
    sinaloa=Estado('Sinaloa', [accS,accO])
    queretaro=Estado('Querétaro', [accN,accE])
    zacatecas=Estado('Zacatecas', [accS,accE])
    
    acciones={'Colima':{'N':jalisco,
                        'O':michoacan},
            'Guanajuato':{'N':zacatecas,
                          'S':michoacan,
                          'E':jalisco,
                          'O':queretaro},
            'Jalisco':{'N':nayarit,
                       'S':colima,
                       'O':guanajuato},
            'Michoacan':{'N':guanajuato,
                         'E':colima},
            'Nayarit':{'N':sinaloa,
                       'S':jalisco,
                       'O':zacatecas},
            'Nuevo León':{'S':queretaro,
                          'E':sinaloa},
            'Sinaloa':{'S':nayarit,
                       'O':nuevoleon},
            'Querétaro':{'N':nuevoleon,
                         'E':guanajuato},
            'Zacatecas':{'S':guanajuato,
                         'E':nayarit}}
    
    objetivo_1=[nuevoleon]
    problema_1=Problema(jalisco,objetivo_1,acciones)
    
    objetivo_2=[michoacan]
    problema_2=Problema(jalisco,objetivo_2,acciones)
    
    objetivo_3=[sinaloa,queretaro]
    problema_3=Problema(jalisco,objetivo_3,acciones)
    
    problema_resolver=problema_1
    
    solucion=anchura(problema_resolver)
    muestra_solucion(solucion)
