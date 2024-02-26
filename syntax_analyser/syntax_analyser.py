from tkinter import filedialog as fd
from lexical_analyser.lexical_analyser import lexical_analyser
from Nodes import ExpressionNode, IdentifierNode, ConstantNode


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


def expression_analyse(instruction: list):
    node_info = []

    for token in instruction:
        if isinstance(token, list):
            node_info.append(expression_analyse(token))
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


def syntax_analyser(tokens):
    instructions = instructions_divider(tokens, 0, True)
    # print(to_list_with_str(instructions))

    root = []
    for instruction in instructions:
        root.append(expression_analyse(instruction))

    # print(len(root))
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
    try:
        syntax_analyser(tokens)
    except Exception as e:
        print(e)
        return


if __name__ == "__main__":
    syntax_output()
