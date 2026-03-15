"""NAMES OF THE AUTHOR(S): Alice Burlats <alice.burlats@uclouvain.be>"""

import random
from lsnode import LSNode
from atom_placement import AtomPlacement
import sys


def random_walk(problem, limit=100) -> LSNode:
    """
    Perform a random walk in the search space and returns a LSNode corresponding to the best found solution.
    """
    current = LSNode(problem, problem.init_state(), 0)
    best = current
    for step in range(limit):
        current = random.choice(list(current.expand()))
        if current.value() < best.value():
            best = current
    return best


def max_value(problem: AtomPlacement, limit=500) -> LSNode:
    """
    Perform a local search by selecting at each iteration the best neighbor of the current state.
    Returns a LSNode corresponding to the best found solution
    """
    result = LSNode(problem=problem, state=problem.init_state(), step=0)
    best_node = result
    min_value = problem.value(result.state)
    for step in range(limit):
        neighbors = problem.neighbors(result.state)

        minNeighbor = neighbors[0]
        min = problem.value(neighbors[0])
        
        for j in range(1, len(neighbors)):

            tmpNeighbor = neighbors[j]
            tmpMin = problem.value(tmpNeighbor)

            if tmpMin < min:
                min = tmpMin
                minNeighbor = tmpNeighbor
        
        result = LSNode(problem=problem, state=minNeighbor, step=step)

        if min < min_value:
            min_value = min
            best_node = result
        

    return best_node


def randomized_max_value(problem: AtomPlacement, limit=500) -> LSNode:
    """
    Perform a local search by randomly selecting a neighbor among the 5 bests
    at each iteration.
    Returns a LSNode corresponding to the best found solution
    """
    result = LSNode(problem=problem, state=problem.init_state(), step=0)
    best_node = result
    min_value = problem.value(result.state)
    for step in range(limit):
        neighbors = problem.neighbors(result.state)

        sortedNeighbors = sorted(neighbors, key=lambda s: problem.value(s))
        selectedNeighbors = sortedNeighbors[:5]
        choice = random.choice(selectedNeighbors)

        result = LSNode(problem=problem, state=choice, step=step)
        current_value = problem.value(result.state)
        if current_value < min_value:
            best_node = result
            min_value = current_value


    return best_node