from os import environ, getenv
from .random_generator import RandomGenerator
from ..analyzers.satSolverAnalyzer import SatSolverAnalyzer

k = int(getenv('K'))
population = int(getenv('POPULATION'))
countOfInitializationFormulas = int(getenv('INITIALIZATION_FORMULAS'))

class InitializedGenerator:
    def generateInitializedFormulas(self):
        formulas = []
        randomGenerator = RandomGenerator()
        analyzer = SatSolverAnalyzer()

        print('\nAnalyzing SAT solver:\n')

        countOfVariables = analyzer.determineCountOfVariables()
        countOfClauses = analyzer.determineCountOfClauses(countOfVariables)

        environ['COUNT_OF_VARIABLES'] = str(countOfVariables)
        environ['COUNT_OF_CLAUSES'] = str(countOfClauses)

        print('\nStarting generating initialization formulas:\n')

        for i in range(countOfInitializationFormulas):
            print('Generated ' + str(i) + ' / ' + str(countOfInitializationFormulas) + ' initialization formula')
            formulas.append(randomGenerator.generateEvenlyRandomFormula(k, countOfVariables, countOfClauses))

        formulas.sort(reverse = True)

        print('\nChosen ' + str(population) + ' the slowest formulas\n')

        return formulas[:population]
