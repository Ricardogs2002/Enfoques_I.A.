"""
El encadenamiento hacia adelante es un método utilizado en sistemas expertos y
la inteligencia artificial para inferir conclusiones a partir de hechos y reglas.

En el encadenamiento hacia adelante, se comienzan con los hechos conocidos y
se buscan reglas que puedan aplicarse a esos hechos para llegar a nuevas
conclusiones. Se continúa aplicando estas reglas sucesivamente hasta que no
se puedan inferir más hechos.

Cada vez que se aplica una regla, se agregan nuevos hechos a una base de
conocimientos. Estos nuevos hechos pueden ser utilizados para aplicar nuevas
reglas y llegar a conclusiones adicionales. Este proceso continúa hasta que
no hay más reglas que se puedan aplicar o se han llegado a todas las
conclusiones posibles."""

# Definir algunos hechos y reglas de ejemplo
hechos = {
    "Paciente tiene fiebre": True,
    "Paciente tiene dolor de cabeza": True,
    "Paciente tiene dolor de garganta": False,
    "Paciente tiene tos": False
}

reglas = {
    ("Paciente tiene fiebre", "Paciente tiene dolor de cabeza"): "Gripe",
    ("Paciente tiene fiebre", "Paciente tiene dolor de garganta"): "Amigdalitis",
    ("Paciente tiene tos", "Paciente tiene fiebre"): "Bronquitis"
}

# Definir la función de encadenamiento hacia adelante
def encadenamiento_hacia_adelante(hechos, reglas):
    # Un bucle que se ejecuta hasta que no se puedan inferir más hechos
    while True:
        hecho_modificado = False
        # Comprobar cada regla
        for regla, enfermedad in reglas.items():
            # Comprobar si todos los hechos necesarios para la regla son verdaderos
            hechos_verdaderos = 0
            for hecho in regla:
                if hecho in hechos and hechos[hecho]:
                    hechos_verdaderos += 1
            # Si se cumplen todos los hechos necesarios, agregar la enfermedad correspondiente a los hechos
            if hechos_verdaderos == len(regla) and enfermedad not in hechos:
                hechos[enfermedad] = True
                hecho_modificado = True
        # Si no se han modificado los hechos en esta iteración, se rompe el bucle
        if not hecho_modificado:
            break
    # Devolver los hechos
    return hechos

# Llamar a la función de encadenamiento hacia adelante con los hechos y reglas definidos anteriormente
enfermedades = encadenamiento_hacia_adelante(hechos, reglas)

# Imprimir los resultados
print("Resultado encadenamiento hacia adelante:")
print(enfermedades)
print("\n")

"""El encadenamiento hacia atrás es otro método utilizado en sistemas expertos
y la inteligencia artificial para inferir conclusiones a partir de hechos y reglas.

A diferencia del encadenamiento hacia adelante, en el encadenamiento hacia
atrás se comienza con una conclusión o objetivo y se busca hacia atrás a
través de las reglas para encontrar los hechos necesarios para llegar a
esa conclusión.

El proceso de encadenamiento hacia atrás comienza con un objetivo y busca en
las reglas para encontrar una regla que tenga esa conclusión como consecuencia.
Si se encuentra una regla, se busca para verificar si los hechos necesarios
para esa regla son verdaderos. Si los hechos necesarios para esa regla no son
verdaderos, se realiza el mismo proceso para encontrar las reglas necesarias
para demostrar los hechos necesarios. Este proceso se repite recursivamente
hasta que se llega a un conjunto de hechos conocidos que se pueden utilizar
para probar el objetivo original."""

# Definir la base de conocimientos con los síntomas y las enfermedades asociadas
base_de_conocimientos = {
    'Síntoma1': ['Enfermedad1', 'Enfermedad2'],
    'Síntoma2': ['Enfermedad1', 'Enfermedad3'],
    'Síntoma3': ['Enfermedad2', 'Enfermedad3'],
    'Síntoma4': ['Enfermedad3']
}

# Definir la meta o objetivo que estamos tratando de determinar
meta = 'Enfermedad1'

# Definir una función para realizar la inferencia de manera recursiva
def encadenamiento_atras(hecho):
    # Comprobar si el hecho es la meta que estamos buscando
    if hecho == meta:
        return True
    # Si el hecho no está en la base de conocimientos, no podemos seguir inferiendo
    elif hecho not in base_de_conocimientos:
        return False
    else:
        # Recorrer todas las enfermedades asociadas con el hecho actual
        for enfermedad in base_de_conocimientos[hecho]:
            # Realizar la inferencia recursivamente para la enfermedad actual
            if encadenamiento_atras(enfermedad):
                # Si encontramos la meta, podemos detener la inferencia y devolver True
                return True
        # Si no encontramos la meta, devolvemos False
        return False

# Ejecutar el programa probando con el síntoma "Síntoma1"
print("Resultado encadenamiento hacia atrás:")
if encadenamiento_atras('Síntoma1'):
    # Si la inferencia es True, imprimir que el paciente probablemente tiene la enfermedad correspondiente a la meta
    print('El paciente probablemente tiene', meta)
else:
    # Si la inferencia es False, imprimir que el paciente no tiene la enfermedad correspondiente a la meta
    print('El paciente no tiene', meta)
