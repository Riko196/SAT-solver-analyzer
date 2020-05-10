from random import randint
from os import getenv

from ..formula.clause import Clause
from ..formula.formula import Formula

class RandomGenerator:
    def generateRandomFormula(self, k, countOfVariables, countOfClauses):
        clauses = []
        for _ in range(countOfClauses):
            literals = []
            for _ in range(k):
                x = randint(1, countOfVariables)
                if (randint(0, 1) == 0):
                    x = -x
                literals.append(x)
            clauses.append(Clause(literals))
        return Formula(clauses, countOfVariables)

    def generateEvenlyRandomFormula(self, k, countOfVariables, countOfClauses):
        distributionOfVariables = [ i for i in range(1, countOfVariables + 1) ]
        rangeOfVariables = countOfVariables
        countOfNegatives = 0
        countOfPositives = 0
        clauses = []
        for _ in range(countOfClauses):
            literals = []
            for _ in range(k):
                index = randint(1, rangeOfVariables)
                takenVariable = distributionOfVariables[index - 1]
                if countOfPositives > countOfNegatives + 10:
                    takenVariable = -takenVariable
                    countOfNegatives += 1
                elif countOfNegatives > countOfPositives + 10:
                    countOfPositives += 1
                elif randint(0, 1) == 0:
                    takenVariable = -takenVariable
                    countOfNegatives += 1
                else:
                    countOfPositives += 1
                literals.append(takenVariable)
                distributionOfVariables[index - 1], distributionOfVariables[rangeOfVariables - 1] = \
                     distributionOfVariables[rangeOfVariables - 1], distributionOfVariables[index - 1]
                rangeOfVariables -= 1
                if rangeOfVariables == 0:
                    rangeOfVariables = countOfVariables
            clauses.append(Clause(literals))
        return Formula(clauses, countOfVariables)
