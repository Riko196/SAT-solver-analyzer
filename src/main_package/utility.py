from time import time
from os import getenv, system

from .generators.genetic_generator import GeneticGenerator
from .analyzers.satSolverAnalyzer import SatSolverAnalyzer

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

def printHardestFormulas(hardestFormulas):
    for index in range(len(hardestFormulas)):
        formula = hardestFormulas[index]
        print('FORMULA' + str(index) + '\n\n')
        print('p cnf ' + str(formula.countOfVariables) + ' ' + str(len(formula.clauses)) + '\n')
        for clause in formula.clauses:
            for literal in clause.literals:
                print(str(literal) + ' ')
                print('0\n\n\n')
