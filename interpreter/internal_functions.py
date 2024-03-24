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


def greater_func(env, a, b):
    a = check_num(a)
    b = check_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'>\' function')
    return a > b


def less_func(env, a, b):
    a = check_num(a)
    b = check_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'<\' function')
    return a < b


def equal_func(env, a, b):
    a = check_num(a)
    b = check_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'=\' function')
    return a == b


def str_greater_func(env, a, b):
    return a > b


def str_less_func(env, a, b):
    return a < b


def str_equal_func(env, a, b):
    return a == b


def str_not_equal_func(env, a, b):
    return a != b


def str_greater_or_equal_func(env, a, b):
    return a >= b


def str_less_or_equal_func(env, a, b):
    return a <= b


INTERNAL_FUNCTIONS = {
    # 'NIL': 'Logical symbol',
    # 'T': 'Logical symbol',
    # 'DEFUN': 'Keyword',
    # 'DEFVAR': 'Keyword',
    'SETQ': 'Keyword',
    'LIST': list_func,
    # 'IF': 'Keyword',
    'COND': 'Keyword',
    'PRINT': print_func,
    'CAR': 'Keyword',
    'CDR': 'Keyword',
    'EMPTY': 'Keyword',
    '+': plus,
    '-': minus,
    '*': 'Arithmetic operator',
    '/': 'Arithmetic operator',
    '>': greater_func,
    '<': less_func,
    '=': equal_func,
    'MOD': 'Arithmetic function',
    'INCF': 'Arithmetic function',
    'DECF': 'Arithmetic function',
    'STRING=': str_equal_func,
    'STRING/=': str_not_equal_func,
    'STRING>': str_less_func,
    'STRING<': str_greater_func,
    'STRING>=': str_greater_or_equal_func,
    'STRING<=': str_less_or_equal_func,
}
