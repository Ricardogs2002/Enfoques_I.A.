# Implementación del encadenamiento hacia adelante

# Definimos las reglas como funciones que reciben un diccionario de síntomas del paciente y devuelven un booleano
def regla1(paciente):
    return paciente["fiebre"] and paciente["dolor de cabeza"] and paciente["tos"]

def regla2(paciente):
    return paciente["dolor de cabeza"] and paciente["fatiga"]

def regla3(paciente):
    return paciente["dolor abdominal"] and paciente["vómitos"]

# Definimos la función de diagnóstico, que recibe un diccionario de síntomas del paciente y devuelve un string con el diagnóstico
def diagnostico(paciente):
    # Aplicamos las reglas secuencialmente, en orden, hasta que alguna se cumpla
    if regla1(paciente):
        return "Gripe"
    elif regla2(paciente):
        return "Resfriado"
    elif regla3(paciente):
        return "Gastroenteritis"
    else:
        return "No se pudo determinar el diagnóstico"

# Creamos un diccionario con los síntomas del paciente
paciente = {"fiebre": True, "dolor de cabeza": True, "tos": True, "fatiga": False, "dolor abdominal": False, "vómitos": False}

# Llamamos a la función de diagnóstico con el diccionario de síntomas del paciente y guardamos el resultado en una variable
resultado = diagnostico(paciente)

# Imprimimos el resultado
print(resultado)

# Nota: el encadenamiento hacia adelante se enfoca en deducir conclusiones a partir de hechos conocidos

