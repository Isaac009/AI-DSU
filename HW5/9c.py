from pgmpy.models import BayesianNetwork
from pgmpy.inference import VariableElimination
from pgmpy.inference.EliminationOrder import WeightedMinFill
from pgmpy.factors.discrete import TabularCPD


alarm_model = BayesianNetwork(
    [
        ("Burglary", "Alarm"),
        ("Earthquake", "Alarm"),
        ("Alarm", "JohnCalls"),
        ("Alarm", "MaryCalls"),
    ]
)

cpd_burglary = TabularCPD(
    variable="Burglary", variable_card=2, values=[[0.99], [0.01]]
)
cpd_earthquake = TabularCPD(
    variable="Earthquake", variable_card=2, values=[[0.98], [0.02]]
)
cpd_alarm = TabularCPD(
    variable="Alarm",
    variable_card=2,
    values=[[0.95, 0.94, 0.29, 0.001], [0.05, 0.06, 0.71, 0.999]],
    evidence=["Burglary", "Earthquake"],
    evidence_card=[2, 2],
)
cpd_johncalls = TabularCPD(
    variable="JohnCalls",
    variable_card=2,
    values=[[0.90, 0.05], [0.1, 0.95]],
    evidence=["Alarm"],
    evidence_card=[2],
)
cpd_marycalls = TabularCPD(
    variable="MaryCalls",
    variable_card=2,
    values=[[0.7, 0.01], [0.3, 0.99]],
    evidence=["Alarm"],
    evidence_card=[2],
)

alarm_model.add_cpds(
    cpd_burglary, cpd_earthquake, cpd_alarm, cpd_johncalls, cpd_marycalls
)

infer = VariableElimination(alarm_model)
g_dist = infer.query(['JohnCalls', 'MaryCalls'])
print(g_dist)
