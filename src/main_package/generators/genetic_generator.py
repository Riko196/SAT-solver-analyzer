from random import randint
from numpy import mean
from os import getenv
from time import time

from ..graph import Graph
from .initialized_generator import InitializedGenerator
from ..formula.clause import Clause
from ..formula.formula import Formula

k = int(getenv('K'))
population = int(getenv('POPULATION'))
iterations = int(getenv('ITERATIONS'))
countOfVariables = int(getenv('COUNT_OF_VARIABLES'))
countOfClauses = int(getenv('COUNT_OF_CLAUSES'))
maximumFileName = getenv('MAXIMUM_FORMULA_FILE')

class GeneticGenerator:
    # population of formulas
    formulas = []

    # number of iterations and average computing time for current formulas
    iterationsAverageComputingTime = []

    # number of iterations and maximum computing time for current formulas
    iterationsMaximumComputingTime = []

    def renderGraph(self):
        graphTitle = 'Computing time (Variables: ' + str(countOfVariables) + ', Clauses: ' \
            + str(countOfClauses) + ', Population: ' + str(population) + ')'
        graph = Graph([ int(i) for i in range(1, iterations + 1)], self.iterationsAverageComputingTime, \
            self.iterationsMaximumComputingTime, graphTitle)
        graph.render()

    def evolveHardestFormulas(self):
        self.initialization()

        print('\nStarting genetic algorithm:')

        for i in range(iterations):
            print('\nIteration: ' + str(i))
            startTime = time()
            self.executeIteration()
            finishTime = time()
            print('Computing Time of iteration: ' + str(finishTime - startTime) + 's')

        self.renderGraph()

        return self.formulas

    def initialization(self):
        initializedGenerator = InitializedGenerator()
        self.formulas = initializedGenerator.generateInitializedFormulas()

    def executeIteration(self):
        computingTimes = []
        for formula in self.formulas:
            if formula.changed:
                computingTimes.append(formula.getComputingTime())
            else:
                computingTimes.append(formula.computingTime)
            formula.changed = False
        average = mean(computingTimes)

        print('Average: ' + str(average) + 's')
        self.iterationsAverageComputingTime.append(average)

        self.selection()

    def selection(self):
        self.formulas.sort(reverse = True)

        print('Maximum: ' + str(self.formulas[0].computingTime) + 's')
        self.iterationsMaximumComputingTime.append(self.formulas[0].computingTime)
        self.formulas[0].printFormula(maximumFileName)

        self.reproduction()

    def reproduction(self):
        for i in range(30, len(self.formulas)):
            mother = self.formulas[randint(0, 29)]
            father = self.formulas[randint(0, 29)]
            child = self.formulas[i]
            child.changed = True
            self.cross(mother, father, child)

    def cross(self, mother, father, child):
        for i in range(len(child.clauses)):
            parent = 0
            if (i % countOfVariables == 0):
                parent = randint(0, 1)
            clause = child.clauses[i]
            parentClause = None
            if parent == 0:
                parentClause = mother.clauses[i]
            else:
                parentClause = father.clauses[i]
            for j in range(k):
                clause.literals[j] = self.mutation(parentClause.literals[j])

    def mutation(self, literal):
        mutate = randint(1, 100)
        if mutate == 1:
            newLiteral = randint(1, countOfVariables)
            if (randint(0, 1) == 0):
                newLiteral = -newLiteral
            return newLiteral
        return literal
