from os import environ, getenv

satSolverCommands = [
    'cryptominisat5 --verb 0 ',
    '/usr/local/lib/glucose-syrup-4.1/simp/glucose_static '
]

def setConstants():
    environ['FORMULA_FILE'] = 'formula.cnf'
    environ['SAT_SOLVER_CMD'] = satSolverCommands[0] + getenv('FORMULA_FILE')
