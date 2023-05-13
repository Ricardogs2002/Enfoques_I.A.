import numpy as np

# Configurar las opciones de advertencias para ignorar las advertencias específicas
np.seterr(divide='ignore', invalid='ignore')

# Datos de entrada
data = np.array([0.5, 1.2, 0.8, np.nan, 1.7, np.nan, 1.5, 2.0])

# Eliminar los valores nulos de los datos
observed_data = data[~np.isnan(data)]

# Inicialización de parámetros
mean = np.nanmean(data)
std = np.nanstd(data)

# Algoritmo EM
while True:
    # Paso E (Expectation)
    # Calcular la probabilidad de los datos observados dado los parámetros actuales
    prob_observed = np.where(std != 0, np.exp(-(observed_data - mean)**2 / (2 * std**2)) / (np.sqrt(2 * np.pi) * std), 0)
    
    # Calcular la probabilidad de los datos faltantes como cero (ya que no se observan)
    prob_missing = np.zeros_like(data)
    prob_missing[np.isnan(data)] = 1
    
    # Paso M (Maximization)
    # Estimar los parámetros actualizados basados en los datos completos y las probabilidades calculadas
    mean_new = np.nansum(data * prob_missing) / np.nansum(prob_missing)
    std_new = np.sqrt(np.nansum((data - mean_new)**2 * prob_missing) / np.nansum(prob_missing))
    
    # Verificar la convergencia
    if np.abs(mean_new - mean) < 1e-6 and np.abs(std_new - std) < 1e-6:
        break
    
    # Actualizar los parámetros
    mean = mean_new
    std = std_new

# Imprimir los parámetros estimados
print("Media:", mean)
print("Desviacion Estandar", std)
