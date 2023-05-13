
#Taxonomías: Categorías y Objetos

#Definimos la taxonomía como un diccionario
taxonomia = {
    'Animales': {
        'Mamíferos': {
            'Perro': {},
            'Gato': {},
            'Elefante': {}
        },
        'Aves': {
            'Águila': {},
            'Pato': {},
            'Pingüino': {}
        },
        'Reptiles': {
            'Serpiente': {},
            'Cocodrilo': {},
            'Tortuga': {}
        }
    },
    'Plantas': {
        'Árboles': {
            'Roble': {},
            'Pino': {},
            'Arce': {}
        },
        'Flores': {
            'Rosa': {},
            'Lirio': {},
            'Tulipán': {}
        }
    }
}

#Función para mostrar la taxonomía
def mostrar_taxonomia(taxonomia, nivel=0):
    for categoria, subcategorias in taxonomia.items():
        print('  ' * nivel + '- ' + categoria)
        if subcategorias:
            mostrar_taxonomia(subcategorias, nivel + 1)

mostrar_taxonomia(taxonomia)
