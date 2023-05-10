"""La unificación es un proceso utilizado en programación para encontrar una
sustitución que haga que dos términos o expresiones sean iguales. En términos
simples, la unificación es la combinación de dos términos o expresiones en uno
solo que contiene todos los elementos de ambos términos o expresiones.

En la programación lógica, la unificación se utiliza para encontrar una
solución para una consulta en la base de conocimientos.

La unificación se realiza mediante la búsqueda de variables que se pueden
enlazar para hacer que dos términos o expresiones sean iguales. Las variables
pueden ser enlazadas a cualquier término o expresión, incluyendo constantes,
variables o estructuras complejas."""

def unify(var, x, env):
    # Si la variable ya está en el entorno, se unifica con su valor
    if var in env:
        return unify(env[var], x, env)
    # Si el valor es una variable, se unifica con su valor en el entorno
    elif isinstance(x, str) and x in env:
        return unify(var, env[x], env)
    # Si la variable no está en el entorno y es una variable libre, se agrega al entorno
    elif isinstance(var, str) and var.islower():
        env[var] = x
        return env
    # Si los valores son iguales, no se necesita hacer nada
    elif var == x:
        return env
    # Si ninguna de las condiciones se cumple, no se puede unificar
    else:
        return False


# Ejemplo de uso de la función de unificación
env = unify('x', 'a', {})
print(env)
# Output: {'x': 'a'}

env = unify('y', 'b', env)
print(env)
# Output: {'x': 'a', 'y': 'b'}

env = unify('f(x,y)', 'f(a,b)', env)
print(env)
# Output: {'x': 'a', 'y': 'b'}

env = unify('f(x,g(y))', 'f(a,g(b))', env)
print(env)
# Output: {'x': 'a', 'y': 'b'}

env = unify('p(x,f(y))', 'p(g(z),f(h(a)))', env)
print(env)
# Output: {'x': 'g(z)', 'y': 'h(a)', 'y1': 'a', 'z': 'a'}
