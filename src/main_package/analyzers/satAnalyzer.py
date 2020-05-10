from numpy import mean, arange
from matplotlib import pyplot

from ..generators.random_generator import RandomGenerator

class SatAnalyzer:
    def __init__(self):
        self.k = 3
        self.countOfVariables = 150
        self.countOfClauses = 630

    def analyzeKSatFormulas(self):
        randomGenerator = RandomGenerator()
        randomFormulasAverageTimes = []

        print('Analyzing k-SAT effectivity')

        for k in range(1, 51):
            print('Analyzing for k = ' + str(k))
            randomFormulasTimes = []
            for i in range(100):
                print('Analyzing formula ' + str(i) + '/100')
                randomFormula = randomGenerator.generateRandomFormula(k, self.countOfVariables, self.countOfClauses)
                randomFormulasTimes.append(randomFormula.computingTime)
            randomFormulasAverageTimes.append(mean(randomFormulasTimes))

        pyplot.bar(arange(50), randomFormulasAverageTimes)
        pyplot.xticks(arange(50), range(1, 51))
        pyplot.xlabel('k')
        pyplot.ylabel('Times(s)')

        pyplot.show()

    def analyzeCountOfClauses(self):
        randomGenerator = RandomGenerator()
        randomFormulasAverageTimes = []

        print('Analyzing count of clauses effectivity')

        for i in arange(1.0, 5.1, 0.1):
            print('Analyzing formulas with ' + str(i) + ' times more clauses than variables')
            randomFormulasTimes = []
            countOfClauses = int(self.countOfVariables * i)
            for j in range(100):
                print('Analyzing formula ' + str(j) + '/100')
                randomFormula = randomGenerator.generateRandomFormula(self.k, self.countOfVariables, countOfClauses)
                randomFormulasTimes.append(randomFormula.computingTime)
            randomFormulasAverageTimes.append(mean(randomFormulasTimes))

        pyplot.bar(arange(50), randomFormulasAverageTimes)
        pyplot.xticks(arange(50), arange(1.0, 5.1, 0.1))
        pyplot.xlabel('k')
        pyplot.ylabel('Times(s)')

        pyplot.show()

    def analyzeRandomAndEvenlyRandomFormulas(self):
        randomGenerator = RandomGenerator()
        randomFormulasAverageTimes = []
        evenlyRandomFormulasAverageTimes = []

        print('Comparing random and evenly random formulas')

        for iteration in range(100):
            print('Iteration: ' + str(iteration))
            randomComputingTimes = []
            evenlyRandomComputingTimes = []
            for formulaId in range(1000):
                print('Formulas ID: ' + str(formulaId))
                randomFormula = randomGenerator.generateRandomFormula(self.k, self.countOfVariables, self.countOfClauses)
                evenlyRandomFormula = randomGenerator.generateEvenlyRandomFormula(self.k, self.countOfVariables, self.countOfClauses)
                randomComputingTimes.append(randomFormula.computingTime)
                evenlyRandomComputingTimes.append(evenlyRandomFormula.computingTime)
            randomFormulasAverageTimes.append(mean(randomComputingTimes))
            evenlyRandomFormulasAverageTimes.append(mean(evenlyRandomComputingTimes))


        pyplot.bar(arange(2) - 0.2, randomFormulasAverageTimes, width = 0.2, color = 'blue', label = 'Random formulas')
        pyplot.bar(arange(2), evenlyRandomFormulasAverageTimes, width = 0.2, color = 'red', label = 'Evenly random formulas')
        pyplot.xticks(arange(2), arange(2))
        pyplot.xlabel('Iteration')
        pyplot.ylabel('Times(s)')
        pyplot.legend(loc="upper left")

        pyplot.show()
