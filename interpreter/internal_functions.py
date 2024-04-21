from interpreter import Environment


def get_num(value):
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
    a = get_num(a)
    b = get_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'+\' function')
    return a + b


def minus(env, a, b):
    a = get_num(a)
    b = get_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'-\' function')
    return a - b


def multiply(env, a, b):
    a = get_num(a)
    b = get_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'*\' function')
    return a * b


def divide(env, a, b):
    a = get_num(a)
    b = get_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'/\' function')
    try:
        return a / b
    except ZeroDivisionError:
        raise Exception('Division by zero')


def truncate(env, a, b):
    a = get_num(a)
    b = get_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'/\' function')
    try:
        return a // b
    except ZeroDivisionError:
        raise Exception('Division by zero')


def mod(env, a, b):
    a = get_num(a)
    b = get_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'MOD\' function')
    try:
        return a % b
    except ZeroDivisionError:
        raise Exception('Division by zero')


def print_func(env, value):
    value = print_internal(value)
    print(value)


def print_internal(value):
    if isinstance(value, bool):
        return 'T' if value is True else 'NIL'
    elif isinstance(value, list):
        if len(value) == 0:
            return 'NIL'
        return f'({" ".join(map(print_internal, value))})'

    return str(value)


def list_func(env, *args):
    return [*args]


def greater_func(env, a, b):
    a = get_num(a)
    b = get_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'>\' function')
    return a > b


def less_func(env, a, b):
    a = get_num(a)
    b = get_num(b)
    if a is None or b is None:
        raise Exception('Wrong arguments for \'<\' function')
    return a < b


def equal_func(env, a, b):
    a = get_num(a)
    b = get_num(b)
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
    if not isinstance(value, list):
        raise Exception('Wrong argument for \'car\' function')
    try:
        res = value[0]
    except IndexError:
        res = False
    return res


def cdr_func(env, value):
    if not isinstance(value, list):
        raise Exception('Wrong argument for \'cdr\' function')
    try:
        res = value[1:]
    except IndexError:
        res = False
    return res


def empty_func(env, value):
    if not isinstance(value, list):
        raise Exception('Wrong argument for \'empty\' function')
    return len(value) == 0


def len_func(env, value):
    if not isinstance(value, list):
        raise Exception('Wrong argument for \'length\' function')
    return len(value)


def push_func(env, lst, value):
    if not isinstance(lst, list):
        raise Exception('Wrong argument for \'push\' function')
    lst.append(value)
    return lst


INTERNAL_FUNCTIONS = {
    'LIST': list_func,
    'PRINT': print_func,
    'CAR': car_func,
    'CDR': cdr_func,
    'EMPTY': empty_func,
    'LENGTH': len_func,
    'PUSH': push_func,
    '+': plus,
    '-': minus,
    '*': multiply,
    '/': divide,
    'TRUNCATE': truncate,
    '>': greater_func,
    '<': less_func,
    '=': equal_func,
    'MOD': mod,
    'STRING=': str_equal_func,
    'STRING/=': str_not_equal_func,
    'STRING>': str_less_func,
    'STRING<': str_greater_func,
    'STRING>=': str_greater_or_equal_func,
    'STRING<=': str_less_or_equal_func,
}
