
"En el enfoque lógico de la inteligencia artificial, la lógica proposicional es una forma "
"de representar y razonar sobre proposiciones y sus interrelaciones utilizando"
"símbolos lógicos. En este contexto, hay tres conceptos fundamentales que"
"se utilizan para evaluar las fórmulas lógicas: equivalencia, validez y satisfacibilidad."

"Equivalencia:"
#La equivalencia en la lógica proposicional se refiere a la relación entre dos 
#fórmulas lógicas que tienen el mismo valor de verdad en todas las interpretaciones
#posibles. Dos fórmulas son equivalentes si y solo si producen los mismos resultados 
#de verdad en todas las situaciones. Se denota por el símbolo de doble implicación (≡). 
#Por ejemplo, la fórmula (p ∧ q) ≡ (q ∧ p) establece que las fórmulas (p ∧ q) y (q ∧ p) 
#son lógicamente equivalentes.

"Validez:"
#La validez se refiere a la propiedad de una fórmula lógica que siempre es verdadera, 
#independientemente de la asignación de verdad a las variables proposicionales.
#Una fórmula es válida si su valor de verdad es verdadero en todas las interpretaciones posibles.
#Por ejemplo, la fórmula (p ∨ ¬p) es válida porque siempre 
#es verdadera sin importar si p es verdadero o falso.

"Satisfacibilidad:"
#La satisfacibilidad se refiere a la propiedad de una fórmula lógica 
#que puede ser verdadera en al menos una interpretación. Una fórmula es
# satisfacible si existe al menos una asignación de verdad a las variables 
#proposicionales que hace que la fórmula sea verdadera. Por ejemplo, la fórmula (p ∧ q) 
#es satisfacible porque puede ser verdadera cuando tanto p como q son verdaderos.

"Ejemplo numerico"

import sympy

# Ejemplo de equivalencia
expresion1 = (3 + 2) == (2 + 3)
expresion2 = 5 == 5
equivalencia = expresion1 == expresion2
print("Equivalencia:", equivalencia)

# Ejemplo de validez
expresion3 = (4 < 5) or (5 < 4)
validez = expresion3
print("Validez:", validez)

# Ejemplo de satisfacibilidad
expresion4 = (1 > 0) and (9 < 10)
satisfacibilidad = sympy.satisfiable(expresion4)
print("Satisfacibilidad:", satisfacibilidad)
