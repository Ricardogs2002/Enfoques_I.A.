#Razonamiento por defecto no monotonico
"""
El razonamiento por defecto no monótonico es una técnica de 
razonamiento lógico que permite a los sistemas de inteligencia artificial
manejar la incertidumbre, la falta de información y la complejidad. 
A diferencia del razonamiento lógico clásico, el razonamiento por
defecto no monótonico no es determinista y no garantiza que las
conclusiones sean verdaderas en todos los casos.

En el razonamiento por defecto no monótonico, se parte de una base
de conocimientos inicial, que puede estar incompleta o ser 
inexacta, y se van añadiendo nuevas reglas y hechos a medida que
se va procesando la información. Las conclusiones que se obtienen
pueden cambiar a medida que se agregan nuevos datos o se 
modifica la base de conocimientos.

En programación, el razonamiento por defecto no monótonico se 
aplica en sistemas de inteligencia artificial para modelar el 
razonamiento humano y manejar la incertidumbre en situaciones en
las que la información es incompleta o no es precisa. Por ejemplo,
se puede utilizar en sistemas de diagnóstico médico para inferir
posibles enfermedades a partir de síntomas y signos, o en sistemas
de recomendación para inferir las preferencias de un usuario a
partir de sus acciones previas.
"""

import dedemo #se importa el módulo dedemo.

# Definir hechos iniciales
hechos = ["A", "B"] #se definen los hechos iniciales A y B.

# Definir las reglas
reglas = [
    "A => B",
    "~A => ~B",
    "~B => C"
]

# Definir la base de conocimientos
base_conocimientos = dedemo.KnowledgeBase(hechos, reglas)
#se crea un objeto KnowledgeBase de dedemo con los hechos y reglas definidos previamente.
#En la octava línea, se utiliza el método get_default_conclusions() de KnowledgeBase para 
#obtener las conclusiones por defecto no monótonico a partir de la base de conocimientos definida.


# Obtener conclusiones por defecto no monótonico
conclusiones = base_conocimientos.get_default_conclusions()
#se definen las reglas utilizando la notación de implicación: "si A entonces B", "si no A entonces no B" y "si no B entonces C".

# Mostrar las conclusiones
print(conclusiones)


