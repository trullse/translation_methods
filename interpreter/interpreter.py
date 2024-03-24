from tkinter import filedialog as fd

from semantic_analyser.semantic_analyser import semantic_analyser
from syntax_analyser.Nodes import *
from internal_functions import *


class Environment:
    def __init__(self, parentEnv=None):
        if parentEnv is None:
            self._init_env()
        else:
            self._env = parentEnv._env.copy()

    def _init_env(self):
        self._env = {}
        for key, value in INTERNAL_FUNCTIONS.items():
            self._env[key] = value

    def get(self, token):
        return self._env[token]

    def set(self, identifier, value):
        self._env[identifier] = value


def prepare_defun(environment, node):
    func_param = node.nodes[2].nodes
    func_name = node.nodes[1].text.upper()
    func_body = node.nodes[3]

    def func(env, *args):
        if len(args) != len(func_param):
            raise Exception('Wrong arguments number')

        inner_env = Environment(env)
        inner_env.set(func_name, func)
        for arg, param in zip(args, func_param):
            inner_env.set(param.text, arg)

        return evaluate(func_body, inner_env)

    environment.set(func_name, func)


def prepare_if(environment, node):
    if_condition = node.nodes[1]
    true_case = node.nodes[2]
    false_case = node.nodes[3]

    if_result = evaluate(if_condition, environment)
    if if_result:
        return evaluate(true_case, environment)
    else:
        return evaluate(false_case, environment)


def evaluate(node, environment):
    if isinstance(node, ConstantNode):
        return node.value
    elif isinstance(node, IdentifierNode):
        try:
            return environment.get(node.text)
        except Exception as e:
            raise Exception(f'Runtime error on line {node.pos}: {e}')
    elif isinstance(node, ExpressionNode):
        function_name = node.nodes[0].text.upper()
        args = node.nodes[1:]
        if function_name == 'DEFVAR':
            environment.set(args[0].text, evaluate(args[1], environment))
        elif function_name == 'DEFUN':
            prepare_defun(environment, node)
        elif function_name == 'IF':
            return prepare_if(environment, node)
        else:
            func = environment.get(function_name)
            args = node.nodes[1:]
            args_evalueted = [evaluate(arg, environment) for arg in args]
            try:
                return func(environment, *args_evalueted)
            except Exception as e:
                raise Exception(f'Runtime error at line {node.nodes[0].pos}: Wrong arguments')
            pass
    else:
        raise Exception('Runtime undefined error')


def interpret_internal(root):
    env = Environment()
    for node in root:
        evaluate(node, env)


if __name__ == "__main__":
    filename = fd.askopenfilename(filetypes=(('txt files', '*.txt'),))
    with open(filename, "r") as f:
        code = f.read()
    try:
        root = semantic_analyser(code)
    except Exception as e:
        print(e)
    print('________________Interpreter______________________')
    interpret_internal(root)
