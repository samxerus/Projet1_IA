"""NAMES OF THE AUTHOR(S): Alice Burlats <alice.burlats@uclouvain.be>"""

from search import *

#####################
#       Launch      #
#####################
if __name__ == '__main__':
    problem = AtomPlacement("instances/i10.txt")
    init_state = problem.init_state()
    step_limit = 100

    node = random_walk(problem, step_limit)
    print("Best solution found (random_walk):")
    print(f"Objective: {node.value()}")
    print(f"State: {node.state}")
    print(f"Steps: {node.step}")

    node = max_value(problem, step_limit)
    print("Best solution found (maxvalue):")
    print(f"Objective: {node.value()}")
    print(f"State: {node.state}")
    print(f"Steps: {node.step}")

    node = randomized_max_value(problem, step_limit)
    print("Best solution found (randomized_maxvalue):")
    print(f"Objective: {node.value()}")
    print(f"State: {node.state}")
    print(f"Steps: {node.step}")