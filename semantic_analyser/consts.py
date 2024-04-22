from enum import Enum


class Types(Enum):
    NUM = 0
    STRING = 1
    BOOL = 2
    LIST = 3
    FUNCTION = 4
    LAMBDA = 5
    UNKNOWN = 6
    SYM = 7


KEY_WORDS = [
    {
        'text': 'DEFVAR',
        'args_num': 2,
        'args_types': [[Types.SYM,], [Types.NUM, Types.LIST, Types.BOOL, Types.STRING, Types.UNKNOWN]],
        'returns': None,
    },
    {
        'text': 'SETQ',
        'args_num': 2,
        'args_types': [
            [Types.SYM, Types.STRING, Types.BOOL, Types.LIST, Types.NUM, Types.UNKNOWN],
            [Types.NUM, Types.LIST, Types.BOOL, Types.LAMBDA, Types.STRING, Types.UNKNOWN]
        ],
        'returns': None,
    },
    {
        'text': 'LIST',
        'args_num': None,
        'args_types': [[Types.NUM, Types.BOOL, Types.STRING, Types.SYM, Types.UNKNOWN, Types.LIST],],
        'returns': Types.LIST,
     },
    {
        'text': 'IF',
        'args_num': 3,
        'args_types': [
            [Types.BOOL,],
            [Types.NUM, Types.LIST, Types.BOOL, Types.STRING, Types.UNKNOWN],
            [Types.NUM, Types.LIST, Types.BOOL, Types.STRING, Types.UNKNOWN]
        ],
        'returns': Types.UNKNOWN,
    },
    {
        'text': 'DEFUN',
        'args_num': 3,
        'args_types': [[Types.FUNCTION], [Types.LIST,], [Types.NUM, Types.LIST, Types.BOOL, Types.STRING, Types.UNKNOWN]],
        'returns': None,
    },
    {
        'text': 'PRINT',
        'args_num': 1,
        'args_types': [[Types.NUM, Types.LIST, Types.BOOL, Types.STRING, Types.UNKNOWN]],
        'returns': Types.UNKNOWN,
    },
    {
        'text': 'CAR',
        'args_num': 1,
        'args_types': [[Types.LIST, Types.UNKNOWN]],
        'returns': Types.UNKNOWN,
    },
    {
        'text': 'CDR',
        'args_num': 1,
        'args_types': [[Types.LIST, Types.UNKNOWN]],
        'returns': Types.LIST,
    },
    {
        'text': 'EMPTY',
        'args_num': 1,
        'args_types': [[Types.LIST, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': 'LENGTH',
        'args_num': 1,
        'args_types': [[Types.LIST, Types.UNKNOWN]],
        'returns': Types.NUM,
    },
    {
        'text': 'PUSH',
        'args_num': 2,
        'args_types': [[Types.LIST, Types.UNKNOWN], [Types.NUM, Types.BOOL, Types.STRING, Types.SYM, Types.UNKNOWN]],
        'returns': Types.LIST,
    },
    {
        'text': 'PROGN',
        'args_num': None,
        'args_types': [[Types.NUM, Types.LIST, Types.BOOL, Types.STRING, Types.UNKNOWN, None]],
        'returns': Types.UNKNOWN,
    },
    {
        'text': '+',
        'args_num': 2,
        'args_types': [[Types.NUM, Types.UNKNOWN], [Types.NUM, Types.UNKNOWN]],
        'returns': Types.NUM,
    },
    {
        'text': '-',
        'args_num': 2,
        'args_types': [[Types.NUM, Types.UNKNOWN], [Types.NUM, Types.UNKNOWN]],
        'returns': Types.NUM,
    },
    {
        'text': '*',
        'args_num': 2,
        'args_types': [[Types.NUM, Types.UNKNOWN], [Types.NUM, Types.UNKNOWN]],
        'returns': Types.NUM,
    },
    {
        'text': '/',
        'args_num': 2,
        'args_types': [[Types.NUM, Types.UNKNOWN], [Types.NUM, Types.UNKNOWN]],
        'returns': Types.NUM,
    },
    {
        'text': 'TRUNCATE',
        'args_num': 2,
        'args_types': [[Types.NUM, Types.UNKNOWN], [Types.NUM, Types.UNKNOWN]],
        'returns': Types.NUM,
    },
    {
        'text': '>',
        'args_num': 2,
        'args_types': [[Types.NUM, Types.UNKNOWN], [Types.NUM, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': '<',
        'args_num': 2,
        'args_types': [[Types.NUM, Types.UNKNOWN], [Types.NUM, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': '=',
        'args_num': 2,
        'args_types': [[Types.NUM, Types.UNKNOWN], [Types.NUM, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': 'MOD',
        'args_num': 2,
        'args_types': [[Types.NUM, Types.UNKNOWN], [Types.NUM, Types.UNKNOWN]],
        'returns': Types.NUM,
    },
    {
        'text': 'STRING=',
        'args_num': 2,
        'args_types': [[Types.STRING, Types.UNKNOWN], [Types.STRING, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': 'STRING/=',
        'args_num': 2,
        'args_types': [[Types.STRING, Types.UNKNOWN], [Types.STRING, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': 'STRING>',
        'args_num': 2,
        'args_types': [[Types.STRING, Types.UNKNOWN], [Types.STRING, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': 'STRING<',
        'args_num': 2,
        'args_types': [[Types.STRING, Types.UNKNOWN], [Types.STRING, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': 'STRING>=',
        'args_num': 2,
        'args_types': [[Types.STRING, Types.UNKNOWN], [Types.STRING, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': 'STRING<=',
        'args_num': 2,
        'args_types': [[Types.STRING, Types.UNKNOWN], [Types.STRING, Types.UNKNOWN]],
        'returns': Types.BOOL,
    },
    {
        'text': 'LOAD',
        'args_num': 1,
        'args_types': [[Types.STRING]],
        'returns': None,
    },
]