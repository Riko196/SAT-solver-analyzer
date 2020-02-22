from os import system, getenv
from time import time
class Formula:
    def __init__(self, clauses, countOfVariables):
        self.clauses = clauses
        self.countOfVariables = countOfVariables
        self.computingTime = self.getComputingTime()

    def __lt__(self, other):
        return self.computingTime < other.computingTime

    def printFormula(self):
        fileName = getenv('FORMULA_FILE')
        with open(fileName, 'w') as file:
            file.write('p cnf ' + str(self.countOfVariables) + ' ' + str(len(self.clauses)) + '\n')
            for clause in self.clauses:
                for literal in clause.literals:
                    file.write(str(literal) + ' ')
                file.write('0\n')

    def getComputingTime(self):
        self.printFormula()
        satSolverCmd = getenv('SAT_SOLVER_CMD')
        startTime = int(time())
        system(satSolverCmd)
        finishTime = int(time())
        self.computingTime = finishTime - startTime
        return self.computingTime