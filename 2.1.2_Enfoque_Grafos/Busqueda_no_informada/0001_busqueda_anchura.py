# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 19:27:54 2023
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
