from tkinter import filedialog as fd
from syntax_analyser.syntax_analyser import *
from .consts import *


def is_num(string):
    if isinstance(string, bool):
        return False
    try:
        float(string)
        return True
    except ValueError:
        return False


def set_return_type(node, variables_scope):
    # print(variables_scope)
    if isinstance(node, ExpressionNode):
        # print('Expression! ' + str(node))
        if node.nodes[0].text.upper() == 'DEFUN':
            # print('Found defun')
            if len(node.nodes[1:]) != 3:
                raise Exception(f'Semantic error on line {node.nodes[0].pos}: '
                                f'Wrong arguments count for defun function')
            args_node = node.nodes[2]
            # print(args_node)
            args_node.return_type = Types.LIST
            for arg_node in args_node.nodes:
                # print(f'found {arg_node}')
                # if arg_node.text in variables_scope:
                #     raise Exception(f'Semantic error on line {arg_node.pos}: '
                #                     f'Wrong parameters for function {node.nodes[0].text}')
                arg_node.return_type = Types.UNKNOWN
                # print(arg_node.return_type)
                variables_scope[arg_node.text] = [Types.UNKNOWN, ]
            variables_scope[node.nodes[1].text] = [Types.FUNCTION, len(args_node.nodes)]
        for child_node in node.nodes:
            set_return_type(child_node, variables_scope.copy())
        if node.nodes[0].return_type == Types.FUNCTION:
            # print('Function')
            found = False
            for word in KEY_WORDS:
                if word['text'] == node.nodes[0].text.upper():
                    # print('Found built-in: ' + word['text'])
                    args = node.nodes[1:]
                    if word['args_num'] is not None and len(args) != word['args_num']:
                        raise Exception(f'Semantic error on line {node.nodes[0].pos}: '
                                        f'Wrong arguments count for function')
                    for i in range(len(args)):
                        if word['args_num'] is not None:
                            args_types = word['args_types'][i]
                        else:
                            args_types = word['args_types'][0]
                        if args[i].return_type not in args_types:
                            tmp = word['args_types'][i]
                            # print(f'Arg: {args[i].text} {args[i].value} {args[i].return_type}')
                            print(f'Return type is {args[i].return_type} and it is not in {tmp}')
                            if args[i].return_type == Types.SYM:
                                raise Exception(f'Semantic error on line {args[i].pos}: '
                                                f'Undefined variable \'{args[i].text}\'')
                            else:
                                pass
                                # raise Exception(f'Semantic error on line {args[i].pos}: '
                                #                 f'Wrong arguments type for function {node.nodes[0].text}')
                    # return type
                    node.return_type = word['returns']
                    # initialization check
                    if word['text'] == 'DEFVAR':
                        variable = node.nodes[1]
                        variables_scope[variable.text] = [node.nodes[2].return_type, ]
                    elif word['text'] == 'SETQ':
                        if node.nodes[1].text not in variables_scope:
                            raise Exception(f'Semantic error on line {node.nodes[1].pos}: '
                                            f'Undefined variable \'{node.nodes[1].text}\'')
                    found = True
                    break
            if not found:
                if node.nodes[0].text in variables_scope:
                    func_info = variables_scope[node.nodes[0].text]
                    if func_info[0] == Types.FUNCTION:
                        args = node.nodes[1:]
                        if len(args) != func_info[1]:
                            raise Exception(f'Semantic error on line {node.nodes[0].pos}: '
                                            f'Wrong arguments count for function {node.nodes[0].text}:'
                                            f' expected {func_info[1]}, found {len(args)}')
                        for i in range(len(args)):
                            if args[i].return_type == Types.SYM:
                                raise Exception(f'Semantic error on line {args[i].pos}: '
                                                f'Undefined variable \'{args[i].text}\'')
                        # return type
                        node.return_type = Types.UNKNOWN
                        found = True
                    else:
                        raise Exception(f'Semantic error on line {node.nodes[0].pos}: '
                                        f'Variable can not be a function {node.nodes[0].text}')
        else:
            if node.return_type is None:
                pass
                # raise Exception(f'Semantic error on line {node.nodes[0].pos}: '
                #                 f'Variable can not be a function {node.nodes[0].text}')
    elif isinstance(node, ConstantNode):
        if is_num(node.value):
            node.return_type = Types.NUM
        elif isinstance(node.value, bool):
            node.return_type = Types.BOOL
        else:
            node.return_type = Types.STRING
        # print('Constant! ' + str(node))
    elif isinstance(node, IdentifierNode):
        ready = False
        for word in KEY_WORDS:
            if word['text'] == node.text.upper():
                # print('Found built-in: ' + word['text'])
                node.return_type = Types.FUNCTION
                ready = True
        if not ready:
            try:
                node_info = variables_scope[node.text]
                node.return_type = node_info[0]
            except Exception as e:
                if node.return_type is None:
                    node.return_type = Types.SYM
        # print('Identifier! ' + str(node))


def semantic_analyser_iternal(root):
    variables_scope = {}  # format:{ name: ['type', 'args_num'], }
    for node in root:
        set_return_type(node, variables_scope)


def semantic_analyser(code):
    root = syntax_analyser(code)
    print('________________Semantic______________________')
    semantic_analyser_iternal(root)
    print('Semantic analyse is done. Everything is ok.')
    return root


if __name__ == "__main__":
    filename = fd.askopenfilename(filetypes=(('txt files', '*.txt'),))
    with open(filename, "r") as f:
        code = f.read()
    try:
        semantic_analyser(code)
    except Exception as e:
        print(e)
