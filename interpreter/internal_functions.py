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
    if isinstance(value, bool):
        print('T' if value is True else 'NIL')
    if isinstance(value, list):
        if len(value) == 0:
            print('NIL')
        print('(' + ' '.join(value) + ')')

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


def car_func(env, value):
    if isinstance(value, list):
        raise Exception('Wrong argument for \'car\' function')
    try:
        res = value[0]
    except IndexError:
        res = False
    return res


def cdr_func(env, value):
    if isinstance(value, list):
        raise Exception('Wrong argument for \'cdr\' function')
    try:
        res = value[1:]
    except IndexError:
        res = False
    return res


def empty_func(env, value):
    if isinstance(value, list):
        raise Exception('Wrong argument for \'empty\' function')
    return len(value) == 0


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
    'CAR': car_func,
    'CDR': cdr_func,
    'EMPTY': empty_func,
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
