from main_package.constants import setConstants
setConstants()

from main_package.utility import evolveHardestFormulas, printHardestFormulas
from main_package.analyzers.satAnalyzer import SatAnalyzer

if __name__ == "__main__":
    hardestFormulas  = evolveHardestFormulas()
    printHardestFormulas(hardestFormulas)