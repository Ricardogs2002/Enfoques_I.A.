import numpy as np
from numpy.linalg import inv

# Definir parámetros del robot SCARA
l1 = 2.0  # longitud del primer eslabón
l2 = 1.0  # longitud del segundo eslabón

# Definir la matriz de transformación homogénea del robot
def get_fk(theta1, theta2):
    T01 = np.array([
        [np.cos(theta1), -np.sin(theta1), 0, 0],
        [np.sin(theta1), np.cos(theta1), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    T12 = np.array([
        [np.cos(theta2), -np.sin(theta2), l1, 0],
        [np.sin(theta2), np.cos(theta2), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    T23 = np.array([
        [1, 0, l2, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    T03 = T01 @ T12 @ T23
    return T03

# Definir la cinemática inversa del robot
def get_ik(x, y, z, p, sigma):
    theta1 = np.arctan2(y, x)
    D = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    theta2_1 = np.arctan2(np.sqrt(1 - D**2), D)
    theta2_2 = np.arctan2(-np.sqrt(1 - D**2), D)
    T03 = np.array([
        [p[0], p[1], p[2], x],
        [p[3], p[4], p[5], y],
        [p[6], p[7], p[8], z],
        [0, 0, 0, 1]
    ])
    T30 = inv(T03)
    T10 = np.array([
        [np.cos(theta1), -np.sin(theta1), 0, 0],
        [np.sin(theta1), np.cos(theta1), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    T32 = T30 @ T10 @ get_fk(theta1, theta2_1)
    T23 = inv(get_fk(theta1, theta2_2)) @ T30 @ T10
    theta3_1 = np.arctan2(T32[1, 2], T32[0, 2])
    theta3_2 = np.arctan2(T23[1, 2], T23[0, 2])
    # Calcular la probabilidad de cada solución
    p1 = np.exp(-0.5 * (theta2_1 - theta2_2)**2 / sigma**2)
    p2 = np.exp(-0.5 * (theta2_2 - theta2_2)**2 / sigma**2)
    p_total = p1 + p2
    p1 /= p_total
    p2 /= p_total
    # Devolver las soluciones y sus probabilidades
    return [(theta1, theta2_1, theta3_1, p1), (theta1, theta2_2, theta3_2, p2)]

x = 2
y = 0.5
z = 1.0
p = np.eye(3).flatten()
sigma = 0.1
solutions = get_ik(x, y, z, p, sigma)
for sol in solutions:
    print("theta1 = {:.3f}, theta2 = {:.3f}, theta3 = {:.3f}, probability = {:.3f}".format(sol[0], sol[1], sol[2], sol[3]))
    
"""
 La cinemática inversa robotica con probabilidad es un proceso que permite encontrar no sólo la solución
 más probable para los ángulos de las articulaciones necesarios para alcanzar una posición objetivo en el espacio de trabajo, 
 sino también las soluciones menos probables, teniendo en cuenta la incertidumbre en las mediciones y en los ángulos del robot.
 
"""
