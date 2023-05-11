#redes semánticas
"""Las redes semánticas son una forma de representación del conocimiento que
se utiliza en inteligencia artificial y psicología cognitiva para modelar cómo
las personas almacenan, organizan y recuperan información en su memoria.

En una red semántica, los conceptos se representan como nodos y las relaciones
entre ellos se representan como arcos. Cada nodo y arco tiene una etiqueta que
indica su significado semántico. Por ejemplo, en una red semántica que modela
el conocimiento de los animales, los nodos podrían ser los nombres de los
animales y los arcos podrían representar relaciones como "es un" (por ejemplo,
"un perro es un animal") o "come" (por ejemplo, "un león come carne")."""

class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
    
    def add_child(self, node):
        self.children.append(node)
    
    def get_child_names(self):
        return [child.name for child in self.children]

# Crear los nodos de la red semántica
fruit = Node("fruit")
color = Node("color", parent=fruit)
size = Node("size", parent=fruit)
red = Node("red", parent=color)
green = Node("green", parent=color)
small = Node("small", parent=size)
medium = Node("medium", parent=size)
large = Node("large", parent=size)

# Agregar las relaciones
fruit.add_child(color)
fruit.add_child(size)
color.add_child(red)
color.add_child(green)
size.add_child(small)
size.add_child(medium)
size.add_child(large)



# Consultar las características de la manzana
apple = Node("apple", parent=fruit)
print("An apple is a", apple.parent.name)
print("The possible colors of an apple are:", ", ".join(color.get_child_names()))
print("The possible sizes of an apple are:", ", ".join(size.get_child_names()))

# Consultar las características de la naranja
orange = Node("orange", parent=fruit)
print("An orange is a", orange.parent.name)
print("The possible colors of an orange are:", ", ".join(color.get_child_names()))
print("The possible sizes of an orange are:", ", ".join(size.get_child_names()))
print("\n")
print("\n")

#Lógica descriptiva
"""La lógica descriptiva es una subdisciplina de la inteligencia artificial que
se enfoca en representar el conocimiento y el razonamiento mediante lenguajes
formales basados en lógica. En particular, la lógica descriptiva se utiliza
para describir ontologías, que son esquemas formales que representan los
conceptos y las relaciones entre ellos en un dominio de conocimiento
específico.

La lógica descriptiva se utiliza para construir sistemas de conocimiento que
pueden razonar y tomar decisiones en base a ese conocimiento. Estos sistemas
pueden ser utilizados en una variedad de aplicaciones, como la minería de
datos, la web semántica, la inteligencia artificial basada en conocimiento y
la robótica, entre otros."""

# Definir la ontología
ontologia = {
    "clases": {
        "Animal": set(),  # Clase padre
        "Mamifero": set(),  # Clase hija de Animal
        "Ave": set(),  # Clase hija de Animal
        "Carnivoro": set(),  # Clase hija de Mamifero
        "Herbivoro": set()  # Clase hija de Mamifero
    },
    "propiedades": {
        "tieneHabitat": {},  # Propiedad de instancia que describe el hábitat en el que vive un animal
        "come": {}  # Propiedad de instancia que describe los objetos que come un animal
    },
    "instancias": {
        "gato": {"clase": "Mamifero", "come": ["vaca"], "tieneHabitat": "casa"},  # Instancia de Mamifero
        "leon": {"clase": "Carnivoro", "come": ["gato"], "tieneHabitat": "selva"},  # Instancia de Carnivoro
        "vaca": {"clase": "Herbivoro", "come": [], "tieneHabitat": "granja"},  # Instancia de Herbivoro
        "aguila": {"clase": "Ave", "come": ["gato"], "tieneHabitat": "montañas"},  # Instancia de Ave
        "oso": {"clase": "Carnivoro", "come": ["vaca"], "tieneHabitat": "bosque"}  # Instancia de Carnivoro
    }
}

# Definir las funciones para realizar las consultas
def comen(obj, instancias):
    """
    Función que recibe un objeto y una lista de instancias, y devuelve una lista con las instancias que comen ese objeto.
    """
    resultados = []  # Lista de resultados
    for instancia, datos in instancias.items():
        if obj in datos["come"]:
            resultados.append(instancia)  # Si la instancia come el objeto, se agrega a la lista de resultados
    return resultados

def vivenEn(habitat, instancias):
    """
    Función que recibe un hábitat y una lista de instancias, y devuelve una lista con las instancias que viven en ese hábitat.
    """
    resultados = []  # Lista de resultados
    for instancia, datos in instancias.items():
        if datos["tieneHabitat"] == habitat:
            resultados.append(instancia)  # Si la instancia vive en el hábitat, se agrega a la lista de resultados
    return resultados

# Realizar algunas consultas
# Consulta 1: ¿Qué animales comen vacas?
print("¿Qué animales comen vacas?")
animales = comen("vaca", ontologia["instancias"])
if animales:
    for animal in animales:
        print(animal)
else:
    print("Ningún animal come vacas.")

# Consulta 2: ¿Qué animales viven en la selva?
print("\n¿Qué animales viven en la selva?")
animales = vivenEn("selva", ontologia["instancias"])
if animales:
    for animal in animales:
        print(animal)
else:
    print("Ningún animal vive en la selva")
