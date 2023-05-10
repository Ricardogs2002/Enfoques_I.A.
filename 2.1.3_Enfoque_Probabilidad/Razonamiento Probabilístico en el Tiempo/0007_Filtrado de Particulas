import numpy as np
import matplotlib.pyplot as plt

class ParticleFilter:
    def __init__(self, num_particles, initial_state, motion_model, observation_model):
        self.num_particles = num_particles
        self.particles = np.zeros((num_particles, len(initial_state)))
        for i in range(num_particles):
            self.particles[i] = initial_state + np.random.normal(0, 1, len(initial_state))
            #Se crea una matriz de ceros la cual se va llenando con valores randoms entre 0 y 1
            #Esto para obtener el valor incial de cada particula
            #Luego se le agrega peso a todas las particulas
        self.weights = np.ones(num_particles) / num_particles
        self.motion_model = motion_model
        self.observation_model = observation_model
        self.resampling_threshold = num_particles / 2
        self.history = [initial_state]
        #Luego se guarda un historial del mismo
    
    def predict(self, control):
        for i in range(self.num_particles):
            self.particles[i] = self.motion_model(self.particles[i], control) + np.random.normal(0, 1, len(self.particles[i]))
    #Aqui se predice el movimiento de la particula el cual usa un argumento de control y el estado de cada particula
    #Este resultado se agrega a la particula creando una nueva posicion 
    
    def update(self, observation):
        for i in range(self.num_particles):
            self.weights[i] *= self.observation_model(observation, self.particles[i])
        self.weights /= np.sum(self.weights)
        #Se actualiza el peso de las particulas con una iteran y luego se multiplica por el peso de cada particula
    
    def resample(self):
        if np.sum(self.weights ** 2) < self.resampling_threshold:
            indexes = np.random.choice(self.num_particles, self.num_particles, p=self.weights)
            self.particles = self.particles[indexes]
            self.weights = np.ones(self.num_particles) / self.num_particles
            #Se cambia la muestras de particulas si el threshold es mayor que los pesos al cuadrado
    
    def run(self, controls, observations):
        for i in range(len(controls)):
            self.predict(controls[i])
            self.update(observations[i])
            self.resample()
            self.history.append(np.average(self.particles, weights=self.weights, axis=0))


def simple_motion_model(state, control):
    return state + np.array([control[0] * np.cos(state[2]), control[0] * np.sin(state[2]), control[1]])

def simple_observation_model(observation, state):
    distance = observation - np.linalg.norm(state[:2])
    return np.exp(-distance ** 2 / 2)


pf = ParticleFilter(100, [0, 0, 0], simple_motion_model, simple_observation_model)
controls = [(1, 0.1)] * 100
observations = np.random.normal(5, 1, 100)
pf.run(controls, observations)
#Se grafica todo el historial para ver como se fueron prediciendo las particulas
plt.plot([x[0] for x in pf.history], [x[1] for x in pf.history])
plt.show()

"""
El filtrado de partículas se utiliza comúnmente en robótica para localizar un robot en un entorno desconocido a partir de medidas de sensores ruidosos. 
El algoritmo de filtrado de partículas funciona de la siguiente manera: se inicializa un conjunto de partículas, cada una representando una hipótesis sobre el estado latente del robot.
En cada iteración, se predice la posición del robot utilizando un modelo de movimiento y se actualiza la distribución de probabilidad del estado latente utilizando un modelo de observación que compara las medidas de sensores con las hipótesis.
Las partículas con pesos más bajos se eliminan y se reemplazan por nuevas partículas generadas a partir de las partículas con pesos más altos. El proceso se repite hasta que se alcanza una precisión suficiente.
"""
