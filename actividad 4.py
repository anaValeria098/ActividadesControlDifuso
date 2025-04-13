import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

left_sensor = ctrl.Antecedent(np.arange(0, 10, 0.1), 'left_sensor')
front_sensor = ctrl.Antecedent(np.arange(0, 10, 0.1), 'front_sensor')
right_sensor = ctrl.Antecedent(np.arange(0, 10, 0.1), 'right_sensor')
left_motor = ctrl.Consequent(np.arange(0, 1, 0.1), 'left_motor')
right_motor = ctrl.Consequent(np.arange(0, 1, 0.1), 'right_motor')


left_motor['reverse'] = fuzz.trimf(left_motor.universe, [0, 0, 0.5])
left_motor['forward'] = fuzz.trimf(left_motor.universe, [0.5, 1, 1])
right_motor['reverse'] = fuzz.trimf(right_motor.universe, [0, 0, 0.5])
right_motor['forward'] = fuzz.trimf(right_motor.universe, [0.5, 1, 1])

left_sensor['near'] = fuzz.trapmf(left_sensor.universe, [0, 0, 4, 6])
left_sensor['far'] = fuzz.trapmf(left_sensor.universe, [4, 6, 10, 10])
right_sensor['near'] = fuzz.trapmf(right_sensor.universe, [0, 0, 4, 6])
right_sensor['far'] = fuzz.trapmf(right_sensor.universe, [4, 6, 10, 10])
front_sensor['near'] = fuzz.trapmf(front_sensor.universe, [0, 0, 4, 6])
front_sensor['far'] = fuzz.trapmf(front_sensor.universe, [4, 6, 10, 10])

# Reglas completas del sistema de control difuso
rule1 = ctrl.Rule(left_sensor['far'] & front_sensor['far'] & right_sensor['far'], [left_motor['forward'], right_motor['forward']])
rule2 = ctrl.Rule(left_sensor['far'] & front_sensor['far'] & right_sensor['near'], [left_motor['reverse'], right_motor['forward']])
rule3 = ctrl.Rule(left_sensor['far'] & front_sensor['near'] & right_sensor['near'], [left_motor['reverse'], right_motor['forward']])
rule4 = ctrl.Rule(left_sensor['far'] & front_sensor['near'] & right_sensor['far'], [left_motor['forward'], right_motor['reverse']])
rule5 = ctrl.Rule(left_sensor['near'] & front_sensor['near'] & right_sensor['far'], [left_motor['forward'], right_motor['reverse']])
rule6 = ctrl.Rule(left_sensor['near'] & front_sensor['near'] & right_sensor['near'], [left_motor['reverse'], right_motor['reverse']])
rule7 = ctrl.Rule(left_sensor['near'] & front_sensor['far'] & right_sensor['near'], [left_motor['forward'], right_motor['reverse']])
rule8 = ctrl.Rule(left_sensor['near'] & front_sensor['far'] & right_sensor['far'], [left_motor['forward'], right_motor['reverse']])

# Crear el sistema de control con todas las reglas
obstacle_avoidance_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8])
robot_simulation = ctrl.ControlSystemSimulation(obstacle_avoidance_ctrl)

robot_simulation.input['left_sensor'] = 0
robot_simulation.input['front_sensor'] = 0
robot_simulation.input['right_sensor'] = 0
robot_simulation.compute()
print(robot_simulation.output['left_motor'])
print(robot_simulation.output['right_motor'])
left_motor.view(sim=robot_simulation)
right_motor.view(sim=robot_simulation)
print()