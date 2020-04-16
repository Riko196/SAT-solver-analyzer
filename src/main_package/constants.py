from os import environ, getenv

satSolverCommands = [
    'cryptominisat5 --verb 0 ',
    '/usr/local/lib/glucose-syrup-4.1/simp/glucose_static '
]

def setConstants():
    satSolverCommand = satSolverCommands[1]
    environ['K'] = '3'
    environ['POPULATION'] = '100'
    environ['ITERATIONS'] = '100'
    environ['COUNT_OF_VARIABLES'] = '150'
    environ['COUNT_OF_CLAUSES'] = str(int(int(getenv('COUNT_OF_VARIABLES')) * 4.2))
    environ['INITIALIZATION_FORMULAS'] = '1000'
    environ['FORMULA_FILE'] = 'formula.cnf'
    environ['MAXIMUM_FORMULA_FILE'] = 'maximum.cnf'
    environ['SAT_SOLVER_CMD'] = satSolverCommand + getenv('FORMULA_FILE') + ' > /dev/null'
    environ['SAT_SOLVER_MAXIMUM_CMD'] = satSolverCommand + getenv('MAXIMUM_FORMULA_FILE') + ' > /dev/null'
