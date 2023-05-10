import sympy

# Definimos la función de resolución Skolem
def skolem(clauses):
    # Transformamos las cláusulas a forma normal conjuntiva (CNF)
    cnf = to_cnf(clauses)
    
    while True:
        # Obtenemos todas las parejas de cláusulas que puedan resolverse
        pairs = [(i,j) for i in range(len(cnf)) for j in range(i+1,len(cnf))]
        
        for i,j in pairs:
            resolvent = resolve(cnf[i], cnf[j])
            
            # Si las cláusulas resuelven en una cláusula vacía, la fórmula es inválida
            if set() in resolvent:
                return False
            
            # Si la resolución no produce una nueva cláusula, pasamos a la siguiente pareja
            if not resolvent:
                continue
            
            # Si la resolución produce una nueva cláusula, la agregamos a la lista de cláusulas
            cnf.append(resolvent)
        
        # Si no se puede producir una nueva cláusula, la fórmula es válida
        return True

# Definimos la función de transformación a forma normal conjuntiva (CNF)
def to_cnf(clauses):
    # Convertimos las cláusulas a una cadena de texto y luego a una expresión simbólica
    expr = ' & '.join(['(' + ' | '.join(map(str, c)) + ')' for c in clauses])
    expr = sympy.parse_expr(expr)
    
    # Transformamos la expresión simbólica a forma normal conjuntiva (CNF)
    return sympy.to_cnf(expr, simplify=False).args

# Definimos la función de resolución de cláusulas
def resolve(c1, c2):
    # Obtenemos todos los pares de literales complementarios entre las dos cláusulas
    pairs = [(l1,l2) for l1 in c1 for l2 in c2 if l1 == -l2]
    
    # Aplicamos la regla de resolución para cada par de literales complementarios
    resolvents = [set(c1 + c2) - set([l1,l2]) for l1,l2 in pairs]
    
    return resolvents

# Ejemplo de uso
clauses = [[2,2],[-1,3],[-2,3],[-3]]
valid = skolem(clauses)
print(valid)

"""
La idea principal detrás de la resolución Skolem es transformar una fórmula o conjunto de fórmulas en una forma normal conjuntiva (CNF) y luego aplicar la regla de resolución 
de cláusulas para obtener nuevas cláusulas que puedan simplificar la fórmula original. La introducción de constantes de Skolem permite eliminar los cuantificadores existenciales de la fórmula original, 
lo que hace que sea más fácil de manejar y reducir el espacio de búsqueda necesario para demostrar su validez o invalidez.
"""
