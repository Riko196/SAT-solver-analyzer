from formula import Formula
from clause import Clause
from os import getenv

class Generator:
    def __init__(self):
        self.formula = Formula([], 0)

    def printFormula(self):
        fileName = getenv('FORMULA_FILE')
        with open(fileName, 'w') as file:
            file.write('p cnf ' + str(self.formula.countOfVariables) + ' ' + str(len(self.formula.clauses)) + '\n')
            for clause in self.formula.clauses:
                for literal in clause.literals:
                    file.write(str(literal) + ' ')
                file.write('0\n')
