import itertools

def generate_truth_table(variables, expression):
    # Genera todas las combinaciones posibles de valores de verdad para las variables
    truth_values = list(itertools.product([False, True], repeat=len(variables)))
    
    table = []
    for values in truth_values:
        row = list(values)
        # Evalúa la expresión lógica utilizando los valores de verdad actuales
        row.append(eval(expression, dict(zip(variables, values))))
        # Agrega la fila a la tabla de verdad
        table.append(row)
    
    return table

# Definición de variables y expresión lógica
variables = ['P', 'Q']
expression = '(P and Q) or (not P)'

# Generar la tabla de verdad
table = generate_truth_table(variables, expression)

# Mostrar la tabla de verdad
header = variables + [expression]
print(' | '.join(header))
print('-' * len(' | '.join(header)))
for row in table:
    print(' | '.join(str(value) for value in row))
