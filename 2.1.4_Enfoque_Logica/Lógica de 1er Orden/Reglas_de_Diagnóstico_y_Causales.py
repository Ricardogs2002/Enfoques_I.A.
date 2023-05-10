"""
Las reglas de diagnóstico y causales son una técnica de razonamiento que se utiliza en sistemas 
de diagnóstico y resolución de problemas. En el enfoque de lógica del primer orden, las reglas de 
diagnóstico y causales se representan mediante fórmulas lógicas que establecen las relaciones entre 
los síntomas, los problemas y las causas.
"""
% Reglas de diagnóstico y causales en Prolog

% Si el aire acondicionado no enciende, puede ser debido a un problema en el termostato o en el suministro eléctrico
causa_noenciende(X) :- problema_termostato(X).
causa_noenciende(X) :- problema_suministro(X).

% Si el termostato no funciona, el aire acondicionado no encenderá
problema_termostato(X) :- falla_termostato(X).

% Si hay un problema en el suministro eléctrico, el aire acondicionado no encenderá
problema_suministro(X) :- falla_suministro(X).

% Hechos
falla_termostato(termostato1).
falla_suministro(suministro1).
"""
En este programa, hemos definido cuatro reglas y dos hechos. Las reglas son:

-causa_noenciende(X) indica que si hay un problema en el termostato o en el suministro eléctrico, entonces el aire acondicionado no encenderá.
-problema_termostato(X) indica que si hay una falla en el termostato X, entonces el aire acondicionado no encenderá.
-problema_suministro(X) indica que si hay una falla en el suministro eléctrico X, entonces el aire acondicionado no encenderá.

Los hechos que hemos definido son:

falla_termostato(termostato1) indica que el termostato1 tiene un problema.
falla_suministro(suministro1) indica que el suministro1 tiene un problema.
Con estos elementos, podemos consultar el programa en Prolog para obtener más información sobre el problema. Por ejemplo, si 
consultamos causa_noenciende(X)., Prolog nos devolverá X = termostato1 ; X = suministro1., indicando que el problema de que el aire
acondicionado no encienda puede ser debido a un problema en el termostato1 o en el suministro1.
