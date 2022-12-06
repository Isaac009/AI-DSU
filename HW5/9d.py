from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD


model = BayesianModel([('Difficulty', 'Grade'), ('Intelligence', 'Grade'), ('Grade', 'Letter'), ('Intelligence', 'SAT')])
cpd_Difficult = TabularCPD(variable='Difficulty', variable_card=2, values=[[0.6], [0.4]])
cpd_Intelligence = TabularCPD(variable='Intelligence', variable_card=2, values=[[0.7], [0.3]])

cpd_Grade = TabularCPD(variable='Grade', variable_card=3,
                   values=[[0.3, 0.05, 0.9,  0.5],
                           [0.4, 0.25, 0.08, 0.3],
                           [0.3, 0.7,  0.02, 0.2]],
                  evidence=['Intelligence', 'Difficulty'],
                  evidence_card=[2, 2])

cpd_Letter = TabularCPD(variable='Letter', variable_card=2,
                   values=[[0.1, 0.4, 0.99],
                           [0.9, 0.6, 0.01]],
                   evidence=['Grade'],
                   evidence_card=[3])

cpd_SAT = TabularCPD(variable='SAT', variable_card=2,
                   values=[[0.95, 0.2],
                           [0.05, 0.8]],
                   evidence=['Intelligence'],
                   evidence_card=[2])

model.add_cpds(cpd_Difficult, cpd_Intelligence, cpd_Grade, cpd_Letter, cpd_SAT)

infer = VariableElimination(model)
g_dist = infer.query(['Grade'])
print(g_dist)