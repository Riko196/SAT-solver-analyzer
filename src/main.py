from constants import setConstants
from generator import Generator
from os import system

if __name__ == "__main__":
    setConstants()

    generator = Generator()
    formula = generator.evolveHardestFormulas()

    system('rm *.pyc')