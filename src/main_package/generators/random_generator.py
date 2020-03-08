from random import randint
from os import getenv

from ..formula.clause import Clause
from ..formula.formula import Formula

k = int(getenv('K'))
population = int(getenv('POPULATION'))
countOfVariables = int(getenv('VARIABLES'))
countOfClauses = int(countOfVariables * 4.2)

class RandomGenerator:
    def generateRandomFormula(self):
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

    def generateSteadyRandomFormula(self):
        distributionOfVariables = [ i for i in range(1, countOfVariables + 1) ]
        rangeOfVariables = countOfVariables
        countOfNegations = 0
        clauses = []
        for _ in range(countOfClauses):
            literals = []
            for _ in range(k):
                index = randint(1, rangeOfVariables)
                takenVariable = distributionOfVariables[index - 1]
                if (randint(0, 1) == 0 and countOfNegations < (countOfClauses*3)//2):
                    takenVariable = -takenVariable
                    countOfNegations += 1
                literals.append(takenVariable)
                distributionOfVariables[index - 1], distributionOfVariables[rangeOfVariables - 1] = \
                     distributionOfVariables[rangeOfVariables - 1], distributionOfVariables[index - 1]
                rangeOfVariables -= 1
                if rangeOfVariables == 0:
                    rangeOfVariables = countOfVariables
            clauses.append(Clause(literals))
        return Formula(clauses, countOfVariables)

    def generateHardestFormulas(self):
        formulas = []
        for i in range(1000):
            print(i)
            formulas.append(self.generateSteadyRandomFormula())
        formulas.sort(reverse = True)
        return formulas[:population]