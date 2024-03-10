from tkinter import filedialog as fd
from syntax_analyser.syntax_analyser import *
from consts import *


def is_num(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def set_return_type(node, variables_scope):
    print(variables_scope)
    if isinstance(node, ExpressionNode):
        print('Expression! ' + str(node))
        if node.nodes[0].text.upper() == 'LAMBDA':
            print('Found lambda')
            if len(node.nodes[1:]) != 2:
                raise Exception(f'Semantic error on line {node.nodes[0].pos}: '
                                f'Wrong arguments count for lambda function')
            args_node = node.nodes[1]
            print(args_node)
            for arg_node in args_node.nodes:
                print(f'found {arg_node}')
                if arg_node in variables_scope:
                    raise Exception(f'Semantic error on line {arg_node.pos}: '
                                    f'Wrong arguments for lambda function')
                arg_node.return_type = Types.UNKNOWN
                print(arg_node.return_type)
                variables_scope[arg_node.text] = [Types.UNKNOWN, ]
        for child_node in node.nodes:
            set_return_type(child_node, variables_scope.copy())
        if node.nodes[0].return_type == Types.FUNCTION:
            print('Function')
            found = False
            for word in KEY_WORDS:
                if word['text'] == node.nodes[0].text.upper():
                    print('Found built-in: ' + word['text'])
                    args = node.nodes[1:]
                    if len(args) != word['args_num']:
                        raise Exception(f'Semantic error on line {node.nodes[0].pos}: '
                                        f'Wrong arguments count for function {node.nodes[0].text}')
                    for i in range(len(args)):
                        if args[i].return_type not in word['args_types'][i]:
                            tmp = word['args_types'][i]
                            print(f'Return type is {args[i].return_type} and it is not in {tmp}')
                            raise Exception(f'Semantic error on line {args[i].pos}: '
                                            f'Wrong arguments type for function {node.nodes[0].text}')
                    # return type
                    node.return_type = word['returns']
                    # initialization check
                    if word['text'] == 'SETQ' or word['text'] == 'DEFINE':
                        variable = node.nodes[1]
                        if node.nodes[2].return_type == Types.LAMBDA:
                            args_len = len(node.nodes[2].nodes[1].nodes)
                            variables_scope[variable.text] = [Types.FUNCTION, args_len]
                        else:
                            variables_scope[variable.text] = [node.nodes[2].return_type, ]

                    found = True
                    break
            if not found:
                if node.nodes[0].text in variables_scope:
                    func_info = variables_scope[node.nodes[0].text]
                    if func_info[0] == Types.FUNCTION:
                        args = node.nodes[1:]
                        if len(args) != func_info[1]:
                            raise Exception(f'Semantic error on line {node.nodes[0].pos}: '
                                            f'Wrong arguments count for function {node.nodes[0].text}')
                        # return type
                        node.return_type = Types.UNKNOWN
                        found = True
                    else:
                        raise Exception(f'Semantic error on line {node.nodes[0].pos}: '
                                        f'Variable can not be a function {node.nodes[0].text}')
        else:
            node.return_type = Types.LIST
    elif isinstance(node, ConstantNode):
        if is_num(node.value):
            node.return_type = Types.NUM
        else:
            node.return_type = Types.STRING
        print('Constant! ' + str(node))
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
        print('Identifier! ' + str(node))


def semantic_analyser(root):
    variables_scope = {}  # format:{ name: ['type', 'args_num'], }
    for node in root:
        set_return_type(node, variables_scope)


if __name__ == "__main__":
    filename = fd.askopenfilename(filetypes=(('txt files', '*.txt'),))
    root = []
    with open(filename, "r") as f:
        code = f.read()
    try:
        root = syntax_analyser(code)
    except Exception as e:
        print(e)
        exit(0)
    print('________________Semantic______________________')
    print(root)
    semantic_analyser(root)
    print(root)
    for node in root:
        print_nodes(node)
