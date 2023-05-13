from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Definir la estructura de la red bayesiana
model = BayesianModel([('D', 'G'), ('I', 'G'), ('G', 'L'), ('I', 'S')])

# Definir las distribuciones de probabilidad condicional (CPD)
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6], [0.4]])
cpd_i = TabularCPD(variable='I', variable_card=2, values=[[0.7], [0.3]])
cpd_g = TabularCPD(variable='G', variable_card=3, values=[[0.3, 0.05, 0.9, 0.5],
                                                          [0.4, 0.25, 0.08, 0.3],
                                                          [0.3, 0.7, 0.02, 0.2]],
                   evidence=['I', 'D'], evidence_card=[2, 2])
cpd_l = TabularCPD(variable='L', variable_card=2, values=[[0.1, 0.4, 0.99],
                                                          [0.9, 0.6, 0.01]],
                   evidence=['G'], evidence_card=[3])
cpd_s = TabularCPD(variable='S', variable_card=2, values=[[0.95, 0.2],
                                                          [0.05, 0.8]],
                   evidence=['I'], evidence_card=[2])

# Asignar las CPD al modelo
model.add_cpds(cpd_d, cpd_i, cpd_g, cpd_l, cpd_s)

# Verificar si la red bayesiana es válida
print(model.check_model())

# Realizar inferencia con la red bayesiana
from pgmpy.inference import VariableElimination

# Crear un objeto de inferencia utilizando el método de eliminación de variables
inference = VariableElimination(model)

# Realizar inferencia de la probabilidad P(G='good' | I='intel', D='dumb')
query = inference.query(variables=['G'], evidence={'I': 1, 'D': 0})
print(query.variables[0])
print(query.values)

# Realizar inferencia de la probabilidad P(L='bad' | G='good')
query = inference.query(variables=['L'], evidence={'G': 0})
print(query.variables[0])
print(query.values)
