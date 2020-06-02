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
    pathToFile = getenv('HARDES_INSTANCES_FILE')
    with open(pathToFile, 'w') as file:
        for index in range(len(hardestFormulas)):
            formula = hardestFormulas[index]
            file.write('FORMULA' + str(index) + '\n')
            file.write('COMPUTING TIME: ' + str(formula.computingTime) + 's\n\n')
            file.write('p cnf ' + str(formula.countOfVariables) + ' ' + str(len(formula.clauses)) + '\n')
            for clause in formula.clauses:
                for literal in clause.literals:
                    file.write(str(literal) + ' ')
                file.write('0\n')
            file.write('\n\n\n')
