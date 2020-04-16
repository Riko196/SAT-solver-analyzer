from os import system, getenv
from time import time

class Formula:
    def __init__(self, clauses, countOfVariables):
        self.clauses = clauses
        self.countOfVariables = countOfVariables
        self.computingTime = self.getComputingTime()
        self.changed = False

    def __lt__(self, other):
        return self.computingTime < other.computingTime

    def printFormula(self, pathToFile):
        with open(pathToFile, 'w') as file:
            file.write('p cnf ' + str(self.countOfVariables) + ' ' + str(len(self.clauses)) + '\n')
            for clause in self.clauses:
                for literal in clause.literals:
                    file.write(str(literal) + ' ')
                file.write('0\n')

    def getComputingTime(self):
        self.printFormula(getenv('FORMULA_FILE'))
        satSolverCmd = getenv('SAT_SOLVER_CMD')
        startTime = time()
        system(satSolverCmd)
        finishTime = time()
        self.computingTime = finishTime - startTime
        return self.computingTime
