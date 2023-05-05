# Definimos las reglas como funciones que reciben un diccionario de síntomas del paciente y devuelven un booleano
def regla1(paciente):
    return paciente["fiebre"] and paciente["dolor de cabeza"] and paciente["tos"]

def regla2(paciente):
    return paciente["dolor de cabeza"] and paciente["fatiga"]

def regla3(paciente):
    return paciente["dolor abdominal"] and paciente["vómitos"]

# Definimos la función de diagnóstico, que recibe un diccionario de síntomas del paciente y devuelve un string con el diagnóstico
def diagnostico(paciente):
    # Si el paciente tiene fiebre, asumimos que puede tener gripe o algo relacionado
    if paciente["fiebre"]:
        # Si el paciente tiene dolor de cabeza y tos, asumimos que tiene gripe
        if paciente["dolor de cabeza"] and paciente["tos"]:
            return "Gripe"
        # Si no, seguimos evaluando
        else:
            # Si el paciente tiene fatiga y dolor de cabeza, asumimos que tiene resfriado
            if paciente["fatiga"] and paciente["dolor de cabeza"]:
                return "Resfriado"
            # Si no, no podemos llegar a una conclusión definitiva
            else:
                return "No se pudo determinar el diagnóstico"
    # Si el paciente no tiene fiebre, asumimos que puede tener gastroenteritis o algo relacionado
    else:
        # Si el paciente tiene dolor abdominal y vómitos, asumimos que tiene gastroenteritis
        if paciente["dolor abdominal"] and paciente["vómitos"]:
            return "Gastroenteritis"
        # Si no, no podemos llegar a una conclusión definitiva
        else:
            return "No se pudo determinar el diagnóstico"

# Creamos un diccionario con los síntomas del paciente
paciente = {"fiebre": True, "dolor de cabeza": True, "tos": True, "fatiga": False, "dolor abdominal": False, "vómitos": False}

# Llamamos a la función de diagnóstico con el diccionario de síntomas del paciente y guardamos el resultado en una variable
resultado = diagnostico(paciente)

# Imprimimos el resultado
print(resultado)

# El encadenamiento hacia atrás se enfoca en determinar qué hechos deben ser verdaderos para que una conclusión sea cierta
