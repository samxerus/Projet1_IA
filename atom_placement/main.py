"""NAMES OF THE AUTHOR(S): Alice Burlats <alice.burlats@uclouvain.be>"""

from search import *
import time


#####################
#       Launch      #
#####################
import time

def run_multiple_times(func, problem, step_limit, runs=10):
    total_value = 0
    total_steps = 0
    total_time = 0

    for _ in range(runs):
        start_time = time.time()
        node = func(problem, step_limit)
        elapsed = time.time() - start_time

        total_value += node.value()
        total_steps += node.step
        total_time += elapsed

    avg_value = total_value / runs
    avg_steps = total_steps / runs
    avg_time = total_time / runs

    return avg_value, avg_steps, avg_time

if __name__ == '__main__':
    problem = AtomPlacement("instances/i10.txt")
    init_state = problem.init_state()
    step_limit = 100
    runs = 10

    avg_value, avg_steps, avg_time = run_multiple_times(random_walk, problem, step_limit, runs)
    print("Random Walk (10 runs) average:")
    print(f"Objective: {avg_value}")
    print(f"Steps: {avg_steps}")
    print(f"Time: {avg_time:.4f} s\n")

    avg_value, avg_steps, avg_time = run_multiple_times(max_value, problem, step_limit, runs)
    print("Max Value (10 runs) average:")
    print(f"Objective: {avg_value}")
    print(f"Steps: {avg_steps}")
    print(f"Time: {avg_time:.4f} s\n")

    avg_value, avg_steps, avg_time = run_multiple_times(randomized_max_value, problem, step_limit, runs)
    print("Randomized Max Value (10 runs) average:")
    print(f"Objective: {avg_value}")
    print(f"Steps: {avg_steps}")
    print(f"Time: {avg_time:.4f} s")