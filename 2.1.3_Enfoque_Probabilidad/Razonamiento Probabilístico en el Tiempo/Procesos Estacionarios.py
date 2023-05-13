
#Proceso Estacionario

#Este proceso es un proceso aleatorio, en el cual las propiedades estadisticas se mantienen
#constantes a lo largo del tiempo, por lo que las caracteristicas como la media, varianza y
#covarianza no dependen del tiempo y son consientes a lo largo de las etapas del proceso

"En este programa generare numeros aleatorios mediante este proceso"

import random

#Genera una secuencia de números aleatorios
def generar_secuencia_aleatoria(n):
    secuencia = []
    for _ in range(n):
        numero = random.randint(1, 100)
        secuencia.append(numero)
    return secuencia

#Verifica si una secuencia es estacionaria
def es_secuencia_estacionaria(secuencia):
    media = sum(secuencia) / len(secuencia)
    varianza = sum((x - media) ** 2 for x in secuencia) / len(secuencia)
    return varianza < 10  #Condicion para que sea o no estacionaria "<" o ">"

#Genera una secuencia de números aleatorios y verificar si es estacionaria
secuencia_aleatoria = generar_secuencia_aleatoria(10)
print("Secuencia generada:", secuencia_aleatoria)
if es_secuencia_estacionaria(secuencia_aleatoria):
    print("La secuencia es estacionaria.")
else:
    print("La secuencia no es estacionaria.")
