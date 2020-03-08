from main_package.constants import setConstants
setConstants()

from main_package.generators.genetic_generator import GeneticGenerator
from main_package.formula.formula import Formula

if __name__ == "__main__":
    generator = GeneticGenerator()
    formula = generator.evolveHardestFormulas()
