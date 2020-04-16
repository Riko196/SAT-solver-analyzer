from time import time
from os import getenv, system

from .generators.genetic_generator import GeneticGenerator
from .analyzer.analyzer import Analyzer

def getMaximumFormulaTime():
    satSolverCmd = getenv('SAT_SOLVER_MAXIMUM_CMD')
    startTime = time()
    system(satSolverCmd)
    finishTime = time()
    return finishTime - startTime

def getFormulaTime():
    satSolverCmd = getenv('SAT_SOLVER_CMD')
    startTime = time()
    system(satSolverCmd)
    finishTime = time()
    return finishTime - startTime

def evolveHardestFormulas():
    return GeneticGenerator().evolveHardestFormulas()

def analyzeHardestFormulas(hardestFormulas):
    Analyzer().analyzeHardestFormulas(hardestFormulas)

def storeHardestFormulas(hardestFormulas):
    for index in range(len(hardestFormulas)):
        hardestFormulas[index].printFormula('generators/formula' + str(index) + '.cnf')