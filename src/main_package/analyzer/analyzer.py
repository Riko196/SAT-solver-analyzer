from random import randint
from numpy import mean

from ..formula.clause import Clause
from ..formula.formula import Formula
from ..generators.random_generator import RandomGenerator

class Analyzer:
    def determineCountOfVariables(self):
        left = 10
        right = 200
        countOfTestFormulas = 200
        while (right - left) > 1:
            countOfVariables = (left + right) // 2
            countOfClauses = int(countOfVariables * 4.2)
            randomGenerator = RandomGenerator()

            formulasComputingTime = []

            for i in range(countOfTestFormulas):
                print('Generated ' + str(i) + ' / ' + str(countOfTestFormulas) + ' initialization formula for '
                'determining count of variables, actual generating for ' + str(countOfVariables) + ' variables')
                formulasComputingTime.append(randomGenerator. \
                    generateSteadyRandomFormula(countOfVariables, countOfClauses).computingTime)
            print('Average: ', mean(formulasComputingTime))
            if mean(formulasComputingTime) > 0.5:
                right = countOfVariables
            else:
                left = countOfVariables

        print('Count of variables analysed, optimal count is ' + str(right))
        return right

    def determineCountOfClauses(self, countOfVariables):
        print('Count of claused analysed, optimal count is ' + str(int(countOfVariables * 4.2)))
        return int(countOfVariables * 4.2)

    def analyzeFormula(self, formula):
        print('Computing time:', formula.computingTime)
        print('Count of clauses:', len(formula.clauses))
        print('Count of variables:', formula.countOfVariables)
        variables = [ 0 for i in range(formula.countOfVariables) ]
        negations = [ 0 for i in range(formula.countOfVariables) ]

        for clause in formula.clauses:
            for lit in clause.literals:
                if lit < 0:
                    negations[abs(lit) - 1] += 1
                variables[abs(lit) - 1] += 1

        print(variables)
        print('Count of negations:', sum(negations))
        print(negations)

    def analyzeHardestFormulas(self, hardestFomulas):
        pass
    #for formula in hardestFomulas:
     #       for clause in formula:
      #          for literal in formula:
