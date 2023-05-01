#por ejemplo spongamos que tenemos un modelo describe la probabilidad de 
#que un paciente tenga una enfermedad en función de sus síntomas.
# El modelo se define mediante con las siguientes variables aleatorias:

#S: Síntomas (Sí o No)
#D: Enfermedad (Sí o No)
#Además, se conocen las siguientes probabilidades condicionales:

#P(D = Sí) = 0.01
#P(D = No) = 0.99
#P(S = Sí | D = Sí) = 0.8
#P(S = Sí | D = No) = 0.1
#Supongamos que un paciente tiene síntomas y queremos calcular la 
#probabilidad de que tenga la enfermedad, es decir, P(D = Sí | S = Sí).

#Podemos utilizar la inferencia por enumeración para calcular esta 
#probabilidad. La idea es enumerar todos los posibles estados 
#de las variables aleatorias (en este caso, hay 4 posibles estados: 
#D = Sí y S = Sí, D = Sí y S = No, D = No y S = Sí, D = No y S = No)
#, y calcular la probabilidad conjunta de cada estado utilizando las 
#probabilidades condicionales del modelo Bayesiano. Luego, 
#podemos sumar las probabilidades de los estados donde 
#D = Sí y dividir entre la suma de las probabilidades de todos los estados donde S = Sí:


# Definimos las probabilidades condicionales
P_D_si = 0.01
P_D_no = 0.99
P_S_si_D_si = 0.8
P_S_si_D_no = 0.1

# Enumeramos los posibles estados
estados = [(True, True), (True, False), (False, True), (False, False)]

# Calculamos la probabilidad conjunta de cada estado
P = {}
for d, s in estados:
    if d:
        P[(d, s)] = P_D_si * P_S_si_D_si if s else P_D_si * (1 - P_S_si_D_si)
    else:
        P[(d, s)] = P_D_no * P_S_si_D_no if s else P_D_no * (1 - P_S_si_D_no)

# Calculamos la probabilidad de que D sea Sí dado que S es Sí
P_D_si_S_si = sum([P[(d, s)] for d, s in estados if d and s]) / sum([P[(d, s)] for d, s in estados if s])

print("La probabilidad de que el paciente tenga la enfermedad dado que tiene síntomas es:", P_D_si_S_si)


