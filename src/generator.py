from formula import Formula
from clause import Clause
from random import randint
from graph import Graph
from numpy import mean

class Generator:
    # population of formulas
    formulas = []

    # number of iterations and average computing time for current formulas
    iterationsAverageComputingTime = []

    def generateRandomFormula(self):
        countOfVariables = 100
        countOfClauses = int(countOfVariables * 4.2)
        clauses = []
        print(countOfClauses)
        for i in range(countOfClauses):
            literals = []
            for _ in range(3):
                x = randint(1, countOfVariables)
                if (randint(0, 1) == 0):
                    x = -x
                literals.append(x)
            clauses.append(Clause(literals))
        return Formula(clauses, countOfVariables)

    def evolveHardestFormulas(self):
        self.initialization()
        for i in range(100):
            print('Iteration:', i)
            self.executeIteration()

        graph = Graph([ int(i) for i in range(1, 101)], self.iterationsAverageComputingTime)
        graph.render()

        return self.formulas

    def initialization(self):
        for i in range(300):
            print('Initialization:', i)
            formula = self.generateRandomFormula()
            self.formulas.append(formula)

    def executeIteration(self):
        computingTimes = [ formula.computingTime for formula in self.formulas ]
        average = mean(computingTimes)
        self.iterationsAverageComputingTime.append(average)
        self.selection()

    def selection(self):
        self.formulas.sort(reverse = True)
        slowestFormulas = self.formulas[:20]
        self.reproduction(slowestFormulas)

    def reproduction(self, slowestFormulas):
        for i in range(20, len(self.formulas)):
            formula = self.formulas[i]
            for j in range(len(formula.clauses)):
                parent = randint(0, 19)
                parentClause = self.formulas[parent].clauses[j]
                clause = formula.clauses[j]
                self.cross(parentClause, clause)
            formula.getComputingTime()

    def cross(self, parentClause, clause):
        for i in range(3):
            clause.literals[i] = parentClause.literals[i]
            clause.literals[i] = self.mutation(clause.literals[i])

    def mutation(self, literal):
        mutate = randint(1, 100)
        if mutate == 1:
            newLiteral = randint(1, 20)
            if (randint(0, 1) == 0):
                newLiteral = -newLiteral
            return newLiteral
        return literal
