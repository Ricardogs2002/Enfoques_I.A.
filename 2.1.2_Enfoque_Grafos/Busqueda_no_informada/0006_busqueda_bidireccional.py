from queue import Queue  #queue es la representación de una cola

# Crear una nueva cola
q = Queue()

# Agregar elementos a la cola
q.put('A')
q.put('B')
q.put('C')

# Obtener el primer elemento de la cola y eliminarlo de la cola
item = q.get()
print(item)  # Resultado: 'A'

# Verificar si la cola está vacía
is_empty = q.empty()
print(is_empty)  # Resultado: False

# Obtener el primer elemento de la cola sin eliminarlo de la cola
item = q.queue[0]
print(item)  # Resultado: 'B'

# Obtener el número de elementos en la cola
size = q.qsize()
print(size)  # Resultado: 2

"""
La búsqueda bidireccional es una técnica utilizada en la 
inteligencia artificial para encontrar una solución óptima 
a un problema, comienza la búsqueda desde el estado inicial y 
el estado objetivo al mismo tiempo, utilizando dos conjuntos de 
nodos: uno desde el estado inicial y otro desde el estado objetivo. 
A medida que la búsqueda avanza, los dos conjuntos de nodos se 
expanden hacia adelante hasta que se encuentran en algún punto intermedio. 

"""
