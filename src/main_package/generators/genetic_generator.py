from random import randint
from numpy import mean
from os import getenv
from time import time

from ..graph import Graph
from .random_generator import RandomGenerator
from ..formula.clause import Clause
from ..formula.formula import Formula

k = int(getenv('K'))
population = int(getenv('POPULATION'))
iterations = int(getenv('ITERATIONS'))
countOfVariables = int(getenv('VARIABLES'))
countOfClauses = int(countOfVariables * 4.2)
maximumFileName = getenv('MAXIMUM_FORMULA_FILE')

class GeneticGenerator:
    # population of formulas
    formulas = []

    # number of iterations and average computing time for current formulas
    iterationsAverageComputingTime = []

    def evolveHardestFormulas(self):
        self.initialization()
        for i in range(iterations):
            startTime = time()
            self.executeIteration()
            finishTime = time()
            print('Iteration:', i, 'Computing Time:', finishTime - startTime)

        graph = Graph([ int(i) for i in range(1, iterations + 1)], self.iterationsAverageComputingTime)
        graph.render()

        return self.formulas

    def initialization(self):
        randomGenerator = RandomGenerator()
        self.formulas = randomGenerator.generateHardestFormulas()

    def executeIteration(self):
        computingTimes = []
        for formula in self.formulas:
            if formula.changed:
                computingTimes.append(formula.getComputingTime())
            else:
                computingTimes.append(formula.computingTime)
            formula.changed = False
        average = mean(computingTimes)

        print('Average:', average)

        self.iterationsAverageComputingTime.append(average)
        self.selection()

    def selection(self):
        self.formulas.sort(reverse = True)

        print('Maximum:', self.formulas[0].computingTime)
        self.formulas[0].printFormula(maximumFileName)

        self.reproduction()

    def reproduction(self):
        for i in range(30, len(self.formulas)):
            mother = self.formulas[randint(0, 29)]
            father = self.formulas[randint(0, 29)]
            formula = self.formulas[i]
            formula.changed = True
            for j in range(len(formula.clauses)):
                parent = 0
                if (j % countOfVariables == 0):
                    parent = randint(0, 1)
                clause = formula.clauses[j]
                parentClause = None
                if parent == 0:
                    parentClause = mother.clauses[j]
                else:
                    parentClause = father.clauses[j]
                self.cross(clause, parentClause)

    def cross(self, clause, parentClause):
        for i in range(k):
            clause.literals[i] = self.mutation(parentClause.literals[i])

    def mutation(self, literal):
        mutate = randint(1, 100)
        if mutate == 1:
            newLiteral = randint(1, countOfVariables)
            if (randint(0, 1) == 0):
                newLiteral = -newLiteral
            return newLiteral
        return literal