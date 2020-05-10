from numpy import mean, arange
from matplotlib import pyplot

from ..generators.random_generator import RandomGenerator
from .bar import Bar
class SatAnalyzer:
    def __init__(self):
        self.k = 3
        self.countOfVariables = 150
        self.countOfClauses = 630

    def analyzeKSatFormulas(self, countOfIterations, countOfFormulas):
        randomGenerator = RandomGenerator()
        randomFormulasAverageTimes = []

        print('Analyzing k-SAT effectivity')

        for k in range(1, countOfIterations + 1):
            print('Analyzing for k = ' + str(k))
            randomFormulasTimes = []
            for i in range(countOfFormulas):
                print('Analyzing formula ' + str(i) + ' / ' + str(countOfFormulas))
                randomFormula = randomGenerator.generateRandomFormula(k, self.countOfVariables, self.countOfClauses)
                randomFormulasTimes.append(randomFormula.computingTime)
            randomFormulasAverageTimes.append(mean(randomFormulasTimes))

        bar = Bar(arange(countOfIterations), randomFormulasAverageTimes, [], [], range(1, countOfIterations + 1), 'k')
        bar.render()

    def analyzeCountOfClauses(self, countOfIterations, countOfFormulas):
        randomGenerator = RandomGenerator()
        randomFormulasAverageTimes = []

        print('Analyzing count of clauses effectivity')

        for i in range(1, countOfIterations + 1):
            print('Analyzing formulas with ' + str(i/10) + ' times more clauses than variables')
            randomFormulasTimes = []
            countOfClauses = int(self.countOfVariables * (float(i)/10))
            for j in range(countOfFormulas):
                print('Analyzing formula ' + str(j) + ' / ' + str(countOfFormulas))
                randomFormula = randomGenerator.generateRandomFormula(self.k, self.countOfVariables, countOfClauses)
                randomFormulasTimes.append(randomFormula.computingTime)
            randomFormulasAverageTimes.append(mean(randomFormulasTimes))

        xticks = [ str(float(i)/10) for i in range(1, countOfIterations + 1) ]
        bar = Bar(arange(countOfIterations), randomFormulasAverageTimes, [], [], xticks, 'Multiple clauses')
        bar.render()

    def analyzeRandomAndEvenlyRandomFormulas(self, countOfIterations, countOfFormulas):
        randomGenerator = RandomGenerator()
        randomFormulasAverageTimes = []
        evenlyRandomFormulasAverageTimes = []

        print('Comparing random and evenly random formulas')

        for iteration in range(countOfIterations):
            print('Iteration: ' + str(iteration))
            randomComputingTimes = []
            evenlyRandomComputingTimes = []
            for formulaId in range(countOfFormulas):
                print('Formulas ID: ' + str(formulaId))
                randomFormula = randomGenerator.generateRandomFormula(self.k, self.countOfVariables, self.countOfClauses)
                evenlyRandomFormula = randomGenerator.generateEvenlyRandomFormula(self.k, self.countOfVariables, self.countOfClauses)
                randomComputingTimes.append(randomFormula.computingTime)
                evenlyRandomComputingTimes.append(evenlyRandomFormula.computingTime)
            randomFormulasAverageTimes.append(mean(randomComputingTimes))
            evenlyRandomFormulasAverageTimes.append(mean(evenlyRandomComputingTimes))

        bar = Bar(arange(countOfIterations) - 0.2, randomFormulasAverageTimes, arange(countOfIterations), \
            evenlyRandomFormulasAverageTimes, arange(countOfIterations), 'Iteration')
        bar.render()
