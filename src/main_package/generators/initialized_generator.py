from os import getenv
from .random_generator import RandomGenerator

population = int(getenv('POPULATION'))
countOfInitializationFormulas = int(getenv('INITIALIZATION_FORMULAS'))

class InitializedGenerator:
    def generateInitializedFormulas(self):
        formulas = []
        randomGenerator = RandomGenerator()

        for i in range(countOfInitializationFormulas):
            print('Generated ' + str(i) + ' / ' + str(countOfInitializationFormulas) + ' random formula')
            formulas.append(randomGenerator.generateRandomFormula())

        formulas.sort(reverse = True)
        return formulas[:population]