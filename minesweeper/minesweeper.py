"""NAMES OF THE AUTHOR(S): Alice Burlats <alice.burlats@uclouvain.be>"""

from pycsp3 import *


def solve_minesweeper(clues: list[list[int]]) -> list[(int, int)]:
    clear()

    rows = len(clues)
    columns = len(clues[0])

    x =  VarArray(size=[rows, columns], dom=range(-1, 8))
    
    for i in range(rows) :
        for j in range(columns) :
            if clues[i][j] >= 0:
                count = 0
                for ki in range(max(0, i - 1), min(rows - 1, i + 1)):
                    for kj in range(max(0, j - 1), min(rows - 1, j + 1)):
                        if clues[ki][kj] == -1:
                            count += 1
                 
                satisfy(x[i][j] == count)

    satisfy([x[i][j] == clues[i][j] for i in range(rows) for j in range(columns) if clues and clues[i][j] >= 0])

    if solve(solver=CHOCO) is SAT:
        print("SATISFIABLE")
        positions = [(i, j) for i in range(len(x)) for j in range(len(x[0])) if x[i][j] == -1]
        return positions
    else:
        print("UNSATISFIABLE")
        return None


def check_solution(clues: list[list[int]], solution: list[(int, int)]) -> bool:
    n = len(clues)
    m = len(clues[0])
    mines_count = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in solution:
        if clues[x][y] != -1:
            print(f"A mine is placed on a clue at position ({x},{y}), invalid solution")
            return False

        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if 0 <= x+a < n and 0 <= y + b < m and (a != 0 or b != 0):
                    mines_count[x + a][y + b] += 1

    for i in range(n):
        for j in range(m):
            if mines_count[i][j] != clues[i][j] and clues[i][j] != -1:
                print(f"The clue at position ({i},{j}) is not respected: there is {mines_count[i][j]} mines instead of {clues[i][j]}")
                return False

    return True


def parse_instance(input_file: str) -> list[list[int]]:
    with open(input_file) as input:
        lines = input.readlines()
    clues = []
    for line in lines:
        row = []
        for cell in line.strip().split(" "):
            row.append(int(cell))
        clues.append(row)
    return clues


if __name__ == '__main__':
    clues = parse_instance("instances/sat/i02.txt")
    solution = solve_minesweeper(clues)
    if solution is not None:
        if check_solution(clues, solution):
            print("The returned solution is valid")
        else:
            print("The returned solution is not valid")
    else:
        print("No solution found")
