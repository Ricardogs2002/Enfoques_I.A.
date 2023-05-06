# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:27:54 2023
@author: 6E1
"""

# Importamos las clases necesarias para el problema
from Clases_base_Grafos import Accion
from Clases_base_Grafos import Estado
from Clases_base_Grafos import Nodo
from Clases_base_Grafos import Problema

#%%
def anchura(problema):
    # Creamos el nodo raíz y comprobamos si es el objetivo
    raiz = crea_nodo_raiz(problema)
    if problema.es_objetivo(raiz.estado):
        return raiz
    
    # Inicializamos la frontera con el nodo raíz y el conjunto de nodos explorados
    frontera = [raiz,]
    explorados = set()
    
    while True:
        # Imprimimos el estado actual de la frontera y los nodos explorados
        print("frontera: ",[nodo.estado.nombre for nodo in frontera])
        print("explorados: ",[estado.nombre for estado in explorados])
        
        # Si la frontera está vacía, no hay solución
        if not frontera:
            return None
        
        # Extraemos el primer nodo de la frontera y lo marcamos como explorado
        nodo = frontera.pop(0)
        print("escoge: ",nodo.estado.nombre)
        print("-------")
        explorados.add(nodo.estado)
        
        # Si el nodo no tiene acciones posibles, lo ignoramos
        if not nodo.acciones:
            continue
        
        # Creamos nodos hijos para cada acción posible del nodo actual
        for nombre_accion in nodo.acciones.keys():
            accion = Accion(nombre_accion)
            hijo = crea_nodo_hijo(problema, nodo, accion)
            
            # Si el estado del nodo hijo no ha sido explorado ni está en la frontera, lo añadimos a la frontera
            estados_frontera = [nodo.estado for nodo in frontera]
            if(hijo.estado not in explorados and hijo.estado not in estados_frontera):
                if problema.es_objetivo(hijo.estado):
                    return hijo
                frontera.append(hijo)

#%%
def crea_nodo_raiz(problema):
    # Creamos el estado y las acciones posibles para el nodo raíz
    estado_raiz = problema.estado_inicial
    acciones_raiz = {}
    if estado_raiz.nombre in problema.acciones.keys():
        acciones_raiz = problema.acciones[estado_raiz.nombre]
        
    # Creamos el nodo raíz y lo devolvemos
    raiz = Nodo(estado_raiz, None, acciones_raiz, None)
    return raiz

#%%
def crea_nodo_hijo(problema, padre, accion):
    # Obtenemos el estado resultante de aplicar la acción al estado del padre
    nuevo_estado = problema.resultado(padre.estado, accion)
    
    # Obtenemos las acciones posibles para el nuevo estado
    acciones_nuevo = {}
    if nuevo_estado.nombre in problema.acciones.keys():
        acciones_nuevo = problema.acciones[nuevo_estado.nombre]
        
    # Creamos el nodo hijo y lo añadimos a los hijos del padre
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
