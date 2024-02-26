from tkinter import filedialog as fd
from lexical_analyser.lexical_analyser import lexical_analyser
from lexical_analyser.token import Token
# from Nodes.VariableNode import VariableNode
# from Nodes.StatementNode import StatementNode
# from Nodes.ArgsNode import ArgsNode
# from Nodes.CollectionNode import CollectionNode
# from Nodes.FuncOperationNode import FuncOperationNode
from Nodes import ExpressionNode, IdentifierNode, ConstantNode, IdentifierType


# def print_node(node):
#     if type(node) == VariableNode:
#         print(f'Variable: {node.token.text}')
#     elif type(node) == CollectionNode:
#         print('Collection')
#         for op in node.items:
#             print_node(op)
#     elif type(node) == StatementNode:
#         print('Statement')
#         for code in node.codeStrings:
#             print_node(code)
#     elif type(node) == ArgsNode:
#         print('Args')
#         for op in node.items:
#             print_node(op)
#     elif type(node) == FuncOperationNode:
#         print(f'Func {node.func.text} with args')
#         for op in node.operands:
#             print_node(op)
#     else:
#         print('Undefined')


def to_list_with_str(instruction):
    output = []
    for token in instruction:
        if type(token) == list:
            output.append(to_list_with_str(token))
        else:
            output.append(token.text)
    return output


def instructions_divider(tokens, start_index, is_origin=False):
    instructions_list = []
    current_instruction = []

    i = start_index
    while i < len(tokens):
        token = tokens[i]
        if token.text in ('(', ')'):
            if token.text == '(':
                if len(current_instruction) == 0:
                    current_instruction.append(token)
                else:
                    nested_instructions, ind = instructions_divider(tokens, i)
                    current_instruction.append(nested_instructions)
                    i = ind
                    continue
            elif token.text == ')':
                if len(current_instruction) == 0:
                    raise Exception(f"Syntax error on line {token.pos}: Closing bracket before open one")
                else:
                    current_instruction.append(token)
                    if is_origin:
                        instructions_list.append(current_instruction)
                        current_instruction = []
                    else:
                        # print(return_list_tokens(current_instruction))
                        return current_instruction, i + 1
        else:
            current_instruction.append(token)
        i += 1

    if len(current_instruction) != 0:
        print(to_list_with_str(current_instruction))
        raise Exception(f"Syntax error: No closing bracket")

    return instructions_list


def expression_analyse2(instruction: list):
    node_info = []

    for token in instruction:
        if isinstance(token, list):
            node_info.append(expression_analyse2(token))
        elif token.text in ('(', ')'):
            continue
        elif token.value is None:
            node_info.append(IdentifierNode(token))
        else:
            node_info.append(ConstantNode(token))

    if len(node_info) == 0:
        raise Exception(f"Syntax error on line {instruction[0].pos}: Empty instruction")
    if not isinstance(node_info[0], IdentifierNode):
        if isinstance(node_info[0], ExpressionNode):
            line = node_info[0].get_func().pos
            type = 'Expression'
        elif isinstance(node_info[0], ConstantNode):
            line = node_info[0].pos
            type = 'Constant'
        else:
            raise Exception(f"Syntax error on line {node_info[0].pos}: {node_info[0]}")
        raise Exception(f"Syntax error on line {line}: Wrong first argument: expected Identifier, "
                        f"found {type}")
    return ExpressionNode(node_info)


# def expression_analyse(instruction: list, prev_is_lambda=False):
#     node_info = []
#
#     if len(instruction) <= 2:
#         raise Exception(f"Syntax error: Empty instruction")
#     for token in instruction:
#         if type(token) == list:
#             if len(node_info) != 0 and type(node_info[0]) == Token and node_info[0].text == 'lambda':
#                 node_info.append(expression_analyse(token, True))
#             node_info.append(expression_analyse(token))
#         elif token.text in ('(', ')'):
#             continue
#         else:
#             if token.info in ('Keyword', 'Arithmetic operator', 'String operator'):
#                 if len(node_info) != 0:
#                     raise Exception(f"Syntax error on line {token.pos}: Function not in the first position")
#                 else:
#                     node_info.append(token)
#             elif token.info in ('Identifier', 'Numeric constant', 'String constant'):
#                 node_info.append(VariableNode(token))
#             else:
#                 raise Exception(f"Syntax error on line {token.pos}: Some error occured")
#     if type(node_info[0]) == Token:
#         if node_info[0].text == 'list':
#             return CollectionNode(node_info[1:])
#         else:
#             return FuncOperationNode(node_info[0], node_info[1:])
#     elif prev_is_lambda:
#         return ArgsNode(node_info)
#     else:
#         if type(node_info[0]) != Token:
#             print(f'Not token at position {node_info[0].token.pos} {node_info[0].token.text}')
#         return FuncOperationNode(node_info[0].token, node_info[1:])


def syntax_analyser(tokens):
    instructions = instructions_divider(tokens, 0, True)
    print(to_list_with_str(instructions))

    root = []
    for instruction in instructions:
        root.append(expression_analyse2(instruction))

    print(len(root))
    print(root)


def syntax_output():
    filename = fd.askopenfilename(filetypes=(('txt files', '*.txt'),))
    with open(filename, "r") as f:
        code = f.read()
    try:
        tokens = lexical_analyser(code, True)
    except Exception as e:
        print(e)
        return
    print('_______________________________________')
    syntax_analyser(tokens)


if __name__ == "__main__":
    syntax_output()
