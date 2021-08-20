import prob_calculator
from unittest import main

hat = prob_calculator.Hat(blue=4, red=2, green=6, black=10)

probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"green": 1, "blue": 1, "black": 10},
    num_balls_drawn=15,
    num_experiments=10000)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)