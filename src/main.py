from os import system, getenv
from graph import Graph
from time import time
from constants import setConstants
from generator import Generator

if __name__ == "__main__":
    setConstants()
    satSolverCmd = getenv('SAT_SOLVER_CMD')

    generator = Generator()
    generator.printFormula()

    startTime = int(time())
    system(satSolverCmd)
    finishTime = int(time())

    graph = Graph([1, 2], [finishTime - startTime, 2])
    graph.render()

    system('rm *.pyc')