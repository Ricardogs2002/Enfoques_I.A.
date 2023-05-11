import random

# Definir la función objetivo (en este caso devuelve la distancia de trayecto)
def funcion_objetivo(ruta, distancias):
    #zip es una funcion que enlaza 2 listas y vincula los elementos entre ellos haciendo parejas de datos
    #En este caso une la distancia de la ruta 1 con la ruta 1 y asi sucesivamente
    #Despues se suman las distancias
    return sum(distancias[i][j] for i, j in zip(ruta[:-1], ruta[1:]))

# Definir la función de vecindad (intercambio de dos clientes en dos rutas diferentes)
#Se hacen todos las iteraciones definidas para encontrar la mejor ruta
#Recibe una ruta y hace cambios entre dos clientes y si la ruta es mejor la actualiza
def intercambio_clientes(rutas):
    n = len(rutas)
    i, j = random.sample(range(n), 2)
    if len(rutas[i]) == 0 or len(rutas[j]) == 0:
        return intercambio_clientes(rutas)
    c1, c2 = random.choice(rutas[i]), random.choice(rutas[j])
    rutas[i].remove(c1)
    rutas[j].remove(c2)
    rutas[i].append(c2)
    rutas[j].append(c1)
    return rutas

# Algoritmo de búsqueda local
def busqueda_local(vrp_datos, max_iteraciones):
    #Escribe todos los datos en una lista(tupla) en donde...
    #distancias: distancias entre clientes    ,demandas:cantidad de demandas por cliente    ,capacidad:capacidad maxima del vehiculo
    #deposito: hubicacion de paradas       clientes: lista de clientes
    distancias, demandas, capacidad, deposito, clientes = vrp_datos
    #Se crea una lista de rutas del tamaño de capacidad
    #se inicializa en 0
    rutas = [[0] for _ in range(capacidad)]
    #Se crea una lista de clientes sin ruta y se inicializa con todos los clientes
    clientes_no_asignados = clientes.copy()
    #Se mezcla la lista aleatoriamente
    random.shuffle(clientes_no_asignados)
    #Inicia un cliclo para asignar a los clientes aleatoriamente a una ruta sin exceder la capacidad maxima
    for cliente in clientes_no_asignados:
        for ruta in rutas:
            if sum(demandas[cliente] for cliente in ruta) + demandas[cliente] <= capacidad:
                ruta.append(cliente)
                break
    #Crea una lista en la que asigna a todos los clientes de todas las rutas en orden para asi decir que esa es la mejor ruta
    mejor_ruta = [cliente for ruta in rutas for cliente in ruta]
    #Despues de crear una lista aleatoria se llama a la funcion para evaluar la distancia del trayecto
    mejor_valor = funcion_objetivo(mejor_ruta, distancias)
    for i in range(max_iteraciones):
        nuevas_rutas = intercambio_clientes(rutas.copy())
        nueva_ruta = [cliente for ruta in nuevas_rutas for cliente in ruta]
        nuevo_valor = funcion_objetivo(nueva_ruta, distancias)
        if nuevo_valor < mejor_valor:
            mejor_ruta = nueva_ruta
            mejor_valor = nuevo_valor
            rutas = nuevas_rutas
    return mejor_ruta, mejor_valor

# Se definen los datos
distancias = [
    [0, 2, 5, 2, 1],
    [2, 0, 3, 2, 3],
    [5, 3, 0, 3, 2],
    [2, 2, 3, 0, 2],
    [1, 3, 2, 2, 0]
]
demandas = [0, 1, 1, 2, 2]
capacidad = 3
deposito = 0
clientes = [1, 2, 3, 4]
vrp_datos = (distancias, demandas, capacidad, deposito, clientes)
ruta, valor = busqueda_local(vrp_datos, 1000)
print("Ruta óptima:", ruta)
print("Distancia total:", valor)
