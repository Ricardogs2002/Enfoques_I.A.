

from filterpy.kalman import KalmanFilter
import numpy as np

# Crear el filtro de Kalman
filtro = KalmanFilter(dim_x=2, dim_z=1)

# Definir las matrices de transición y observación
filtro.F = np.array([[1., 1.],
                     [0., 1.]])  # Matriz de transición
filtro.H = np.array([[1., 0.]])  # Matriz de observación

# Definir la matriz de covarianza del proceso y de la observación
filtro.Q = np.eye(2) * 0.1  # Covarianza del proceso
filtro.R = np.eye(1) * 1.0  # Covarianza de la observación

# Establecer el estado inicial y la covarianza inicial
filtro.x = np.array([[0.], [0.]])  # Estado inicial
filtro.P = np.eye(2) * 1000.0  # Covarianza inicial

# Observaciones simuladas
observaciones = [1, 2, 3, 4, 5]

# Filtrar las observaciones
for z in observaciones:
    filtro.predict()
    filtro.update(z)

    # Obtener la estimación del estado
    estado_estimado = filtro.x

    print("Estado estimado:", estado_estimado)
