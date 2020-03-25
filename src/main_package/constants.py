from os import environ, getenv

satSolverCommands = [
    'cryptominisat5 --verb 0 ',
    '/usr/local/lib/glucose-syrup-4.1/simp/glucose_static '
]

def setConstants():
    environ['K'] = '3'
    environ['POPULATION'] = '100'
    environ['ITERATIONS'] = '10'
    environ['VARIABLES'] = '150'
    environ['CLAUSES'] = str(int(int(getenv('VARIABLES')) * 4.2))
    environ['INITIALIZATION_FORMULAS'] = '100'
    environ['FORMULA_FILE'] = 'formula.cnf'
    environ['MAXIMUM_FORMULA_FILE'] = 'maximum.cnf'
    environ['SAT_SOLVER_CMD'] = satSolverCommands[1] + getenv('FORMULA_FILE') + ' > /dev/null'
