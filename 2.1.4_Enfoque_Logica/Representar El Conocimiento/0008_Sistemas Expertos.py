# Definir las reglas del sistema experto
reglas = [
    {'clima': 'frio', 'ropa': 'abrigo'},
    {'clima': 'frio', 'ropa': 'sueter'},
    {'clima': 'calido', 'ropa': 'playera'},
    {'clima': 'calido', 'ropa': 'shorts'},
    {'clima': 'muy caliente', 'ropa': 'shorts'},
    {'clima': 'muy caliente', 'ropa': 'ropa ligera'}
]

# Pedir al usuario que ingrese la temperatura
temperatura = float(input("Ingrese la temperatura actual en grados Celsius: "))

# Buscar la ropa adecuada para la temperatura ingresada
ropa_adecuada = None
for regla in reglas:
    if regla['clima'] == 'frio' and temperatura < 10:
        ropa_adecuada = regla['ropa']
        break
    elif regla['clima'] == 'calido' and temperatura >= 10 and temperatura < 30:
        ropa_adecuada = regla['ropa']
        break
    elif regla['clima'] == 'muy caliente' and temperatura >= 30:
        ropa_adecuada = regla['ropa']
        break

# Mostrar la ropa adecuada al usuario
if ropa_adecuada:
    print("La temperatura actual es de", temperatura, "grados Celsius. La ropa adecuada es", ropa_adecuada)
else:
    print("Lo siento, no se puede determinar la ropa adecuada para la temperatura ingresada.")

"""
Los sistemas expertos son un tipo de sistema de inteligencia artificial diseñado para imitar la toma de decisiones humanas en un campo específico de conocimiento.
Estos sistemas utilizan una combinación de reglas, heurísticas y representaciones simbólicas para representar y manipular el conocimiento.
En términos de representación del conocimiento, los sistemas expertos utilizan diferentes enfoques dependiendo del dominio de conocimiento que estén tratando de modelar. 

"""
