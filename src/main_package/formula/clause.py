class Clause:
    def __init__(self, literals):
        self.literals = literals

    def consists(self, variable):
        for literal in self.literals:
            if abs(literal) == variable:
                return True
        return False

    def copy(self, clause):
        for i in len(clause.literals):
            self.literals[i] = clause.literals[i]
