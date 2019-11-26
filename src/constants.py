from os import environ, getenv

def setConstants():
    environ['FORMULA_FILE'] = 'formula.cnf'
    environ['SAT_SOLVER_CMD'] = 'cryptominisat5 --verb 0 ' + getenv('FORMULA_FILE')