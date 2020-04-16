from main_package.constants import setConstants
setConstants()

from main_package.utility import evolveHardestFormulas, analyzeHardestFormulas, storeHardestFormulas

if __name__ == "__main__":
    hardestFormulas  = evolveHardestFormulas()
    analyzeHardestFormulas(hardestFormulas)
    storeHardestFormulas(hardestFormulas)