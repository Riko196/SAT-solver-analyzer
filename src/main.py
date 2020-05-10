from main_package.constants import setConstants
setConstants()

from main_package.utility import evolveHardestFormulas, analyzeHardestFormulas, storeHardestFormulas
from main_package.analyzers.satAnalyzer import SatAnalyzer

if __name__ == "__main__":
    satAnalyzer = SatAnalyzer()
    satAnalyzer.analyzeRandomAndEvenlyRandomFormulas()
    #hardestFormulas  = evolveHardestFormulas()
    #analyzeHardestFormulas(hardestFormulas)
    #storeHardestFormulas(hardestFormulas)