# from interpreter.interpreter import evaluate


def check_num(value):
    if isinstance(value, int) or isinstance(value, float):
        return value
    try:
        return int(value)
    except Exception as e:
        try:
            return float(value)
        except Exception as e:
            return None


def plus(env, a, b):
    a = check_num(a)
    b = check_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'+\' function')
    return a + b


def minus(env, a, b):
    a = check_num(a)
    b = check_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'-\' function')
    return a - b


def print_func(env, value):
    if not (isinstance(value, str) or isinstance(value, int) or isinstance(value, float)):
        raise Exception('Wrong arguments for \'print\' function')
    print(value)
    return value


def list_func(env, *args):
    return args


INTERNAL_FUNCTIONS = {
    'NIL': 'Logical symbol',
    'T': 'Logical symbol',
    # 'DEFUN': 'Keyword',
    # 'DEFVAR': 'Keyword',
    'SETQ': 'Keyword',
    'LIST': list_func,
    'IF': 'Keyword',
    'COND': 'Keyword',
    'PRINT': print_func,
    'CAR': 'Keyword',
    'CDR': 'Keyword',
    'EMPTY': 'Keyword',
    '+': plus,
    '-': minus,
    '*': 'Arithmetic operator',
    '/': 'Arithmetic operator',
    'MOD': 'Arithmetic function',
    'INCF': 'Arithmetic function',
    'DECF': 'Arithmetic function',
    'STRING=': 'String operator',
    'STRING/=': 'String operator',
    'STRING>': 'String operator',
    'STRING<': 'String operator',
    'STRING>=': 'String operator',
    'STRING<=': 'String operator',
}
