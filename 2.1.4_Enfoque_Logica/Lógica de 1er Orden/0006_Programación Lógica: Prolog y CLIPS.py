"""
La programación lógica es un paradigma de programación que se basa en la lógica matemática y la teoría de conjuntos 
para representar y manipular el conocimiento y la información. En la programación lógica, los programas se definen 
en términos de reglas lógicas que describen las relaciones entre los objetos y los eventos del mundo real.

Prolog y CLIPS son dos lenguajes de programación lógica populares utilizados en la inteligencia artificial 
y otras áreas de la informática.

Prolog (Programming in Logic) es un lenguaje de programación lógica que se utiliza en la inteligencia artificial 
y otras aplicaciones que requieren razonamiento automático. En Prolog, los programas se definen en términos de 
reglas lógicas que describen las relaciones entre los objetos y los eventos del mundo real. Prolog es especialmente 
adecuado para la programación de sistemas expertos, la representación de conocimientos y la resolución de problemas.

CLIPS (C Language Integrated Production System) es un sistema de desarrollo de reglas experto basado en la programación 
lógica. CLIPS se utiliza para construir sistemas expertos que pueden realizar inferencias a partir de una base de conocimientos 
y aplicar reglas para tomar decisiones y resolver problemas. CLIPS tiene una sintaxis similar a la de Lisp y se ejecuta en una 
variedad de plataformas, incluyendo Windows, Linux y Mac OS.



Prolog es un lenguaje de programación lógica utilizado principalmente para la inteligencia artificial y el procesamiento del 
lenguaje natural. Se basa en la programación lógica de primer orden, donde se definen hechos y reglas lógicas y se utilizan 
algoritmos de inferencia para llegar a conclusiones y respuestas.

Por otro lado, CLIPS es un sistema experto de producción basado en reglas que se utiliza para modelar problemas y tomar decisiones.
 Es similar a Prolog en el sentido de que ambos utilizan reglas y algoritmos de inferencia para llegar a conclusiones. 
 Sin embargo, CLIPS se enfoca en la construcción de sistemas expertos, mientras que Prolog es más general y puede ser utilizado
 para una amplia gama de aplicaciones de inteligencia artificial.

Otra diferencia importante entre Prolog y CLIPS es que Prolog se basa en la programación lógica de primer orden, mientras que
 CLIPS se basa en la producción de reglas. La programación lógica es más adecuada para la representación y manipulación de conocimiento 
 incierto y ambiguo, mientras que la producción de reglas se utiliza para la toma de decisiones basadas en reglas simples y específicas.
"""



"                                 ejemplo de prolog  "

"""
Supongamos que queremos modelar una base de conocimiento que nos permita deducir si un animal es mamífero o no. 
Para ello, podemos utilizar reglas lógicas que establezcan ciertas características que definen a los mamíferos.

En este caso, podríamos utilizar las siguientes reglas:

Todos los animales que tienen pelo son mamíferos.
Todos los animales que dan leche son mamíferos.

En este ejemplo, hemos definido dos listas que contienen los animales que tienen pelo y los animales que dan leche 
respectivamente. Luego, hemos definido una regla llamada es_mamifero que toma como argumento un animal y devuelve 
True si cumple alguna de las dos características mencionadas anteriormente.

Finalmente, hemos realizado algunas consultas para comprobar el funcionamiento de nuestra regla
"""


# Definimos algunos hechos
tiene_pelo = ["gato", "perro", "vaca"]
da_leche = ["vaca", "cabra"]

# Definimos la regla para determinar si un animal es mamífero
def es_mamifero(animal):
    if animal in tiene_pelo or animal in da_leche:
        return True
    else:
        return False

# Ejemplos de consultas
print(es_mamifero("gato"))  # True
print(es_mamifero("pato"))  # False






"                                       ejemplo de CLIPS                    "


"""

se puede implementar un sistema experto similar a CLIPS en Python utilizando reglas condicionales e iteración manual.

Supongamos que tenemos un problema donde debemos determinar si una persona es apta para una beca en función de su desempeño 
académico y su situación financiera. Primero, definimos las reglas para determinar si una persona es elegible para una beca:

La persona debe tener un promedio mayor o igual a 9.0 y no tener materias reprobadas.
La persona debe tener ingresos menores o iguales a $15,000 pesos mensuales.


En este ejemplo, el usuario ingresa sus datos y luego se evalúan las reglas para determinar si es elegible para la beca. 
Si cumple con ambas reglas, se imprime un mensaje que indica que es elegible. De lo contrario, se imprime un mensaje que 
indica que no es elegible.
"""

# Solicitamos los datos del usuario
nombre = input("Nombre: ")
promedio = float(input("Promedio: "))
materias_reprobadas = int(input("Materias reprobadas: "))
ingresos = float(input("Ingresos mensuales: "))

# Evaluamos las reglas
if promedio >= 90 and materias_reprobadas == 0 and ingresos <= 15000:
    print(f"{nombre} es elegible para la beca.")
else:
    print(f"{nombre} no es elegible para la beca.")
