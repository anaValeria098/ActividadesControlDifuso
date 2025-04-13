
import fuzzylite as fl
import numpy as np

engine = fl.Engine(
    name="TipCalculator",
    # Define input varibles: service and food
    input_variables=[
        fl.InputVariable(
            name="service",
            minimum=0.0,
            maximum=10.0,
            lock_range=False,
            # Three terms for service
            terms=[#fl.Trapezoid("poor", 0.0, 0.0, 2.5, 5.0),
                   #fl.Triangle("good", 2.5, 5.0, 7.5),
                   #fl.Trapezoid("excellent", 5.0, 7.5, 10.0, 10.0)]
                   fl.Gaussian("poor", 0.0, 1.5),
                   fl.Gaussian("good", 5.0, 1.5),
                   fl.Gaussian("excellent", 10.0, 1.5)],
        ),
        fl.InputVariable(
            name="food",
            minimum=0.0,
            maximum=10.0,
            lock_range=False,
            # Two terms for food
            terms=[fl.Trapezoid("rancid", 0.0, 0.0, 1.0, 3.0),
                   fl.Trapezoid("delicious", 7.0, 9.0, 10.0, 10.0)],
        )
    ],
    output_variables=[
        fl.OutputVariable(
            name="tip",
            minimum=0.0,
            maximum=30.0,
            lock_range=False,
            lock_previous=False,
            default_value=fl.nan,
            aggregation=fl.Maximum(),
            defuzzifier=fl.Centroid(resolution=100),
            # Three terms for tip
            terms=[fl.Triangle("cheap", 0.0, 5.0, 10.0),
                   fl.Triangle("average", 10.0, 15.0, 20.0),
                   fl.Triangle("generous", 20.0, 25.0, 30.0)],
        )
    ],
    rule_blocks=[
        fl.RuleBlock(
            name="mamdani",
            conjunction=fl.AlgebraicProduct(),
            disjunction=fl.AlgebraicSum(),
            implication=fl.AlgebraicProduct(),
            activation=fl.General(),
            rules=[
                fl.Rule.create("if service is poor or food is rancid then tip is cheap"),
                fl.Rule.create("if service is good then tip is average"),
                fl.Rule.create("if service is excellent or food is delicious then tip is generous"),
            ],
        )
    ],
)
engine = fl.Engine(
name="TipCalculator",
# Define input varibles: service and food
input_variables=[
fl.InputVariable(
name="service",
minimum=0.0,
maximum=10.0,
lock_range=False,
# Three terms for service
terms=[fl.Trapezoid ("poor", 0.0, 0.0, 2.5, 5.0),
fl.Triangle ("good", 2.5, 5.0, 7.5),
fl.Trapezoid ("excellent", 5.0, 7.5, 10.0, 10.0)],
),
fl.InputVariable(
name="food",
minimum=0.0,
maximum=10.0,
lock_range=False,
# Two terms for food
terms=[fl.Trapezoid("rancid", 0.0, 0.0, 1.0, 3.0),
fl.Trapezoid("delicious", 7.0, 9.0, 10.0, 10.0)],
)
],
output_variables=[
fl.OutputVariable(
name="tip",
minimum=0.0,
maximum=30.0,
lock_range=False,
lock_previous=False,
default_value=fl.nan,
aggregation=fl.Maximum(),
defuzzifier=fl.Centroid(resolution=100),
# Three terms for tip
terms=[fl.Triangle("cheap", 0.0, 7.5,15.0),
fl.Triangle("average", 10.0, 17.5, 25.0),
fl.Triangle("generous", 15.0, 25.0, 30.0)],
)
],
rule_blocks=[
  fl.RuleBlock(
    name="mamdani",
    conjunction= fl.AlgebraicProduct(),
    disjunction= fl.AlgebraicSum(),
    implication= fl.AlgebraicProduct(),
    activation= fl.General(),
    rules=[
    fl.Rule.create("if service is poor or food is rancid then tip is cheap"),
    fl.Rule.create("if service is good then tip is average"),
    fl.Rule.create("if service is excellent or food is delicious then tip is generous"),
    ],
  )
],
)
#testing 
engine.input_variable("service").value=2.0
engine.input_variable("food").value=7.0
engine.process()
print("y=", engine.output_variable("tip").value)
print("z =", engine.output_variable("tip").fuzzy_value())


