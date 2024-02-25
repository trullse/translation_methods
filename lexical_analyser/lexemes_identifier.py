from lexical_analyser.consts import KEY_WORDS, OPERATORS
from prettytable import PrettyTable
from lexical_analyser.token import Token


def check_num(element: str):
    if not element[0].isdigit():
        return False
    if element[0] == '-' and not element[2].isdigit():
        return False
    is_float = False
    for i in range(len(element)):
        if i == 0:
            continue
        elif element[i] == '.':
            if not is_float:
                is_float = True
            else:
                return False
        elif not element[i].isdigit():
            return False
    return True


def check_str(element):
    if not element[0] == '"':
        return False
    if len(element) < 2:
        return False
    if not element[len(element) - 1] == '"':
        return False
    return True


def check_identifier(element: str):
    if not element[0].isalpha():
        return False
    for el in element:
        if not el.isalnum() and el != '-':
            return False
    return True


def check_match(element: str, identifiers):
    ident = [iden.text for iden in identifiers]
    opers = list(OPERATORS.keys())
    keyws = list(KEY_WORDS.keys())

    base = ident + opers + keyws
    max_match = ""
    max_count = 0

    for string in base:
        count = 0
        i = 0
        while i < min(len(string), len(element)):
            if string[i] == element[i]:
                count += 1
            else:
                break
            i += 1
        if count > max_count:
            max_count = count
            max_match = string

    return max_match


def lexemes_identifier(row_list):
    identifiers = []
    consts = []
    lexemes = []
    cur_index = 1
    is_prev_open_bracket = False
    is_prev_lambda = False
    bracket = []
    token_list = []

    for el in row_list:
        cur_el = el['lexeme']

        if cur_el in ('(', ')'):
            # lexemes.append([cur_index, cur_el, 'Operation divider'])
            token = Token(el['line'], cur_index, cur_el, 'Operation divider')
            lexemes.append(token)
            token_list.append(token)
            if len(bracket) == 0 and cur_el == ')':
                raise Exception(f"Lexical error on line {el['line']}: Closing bracket before open one")
            elif cur_el == '(':
                bracket.append(cur_el)
                if not is_prev_lambda:
                    is_prev_open_bracket = True
            else:
                bracket.pop()
                is_prev_open_bracket = False
            cur_index += 1
        else:
            is_prev_lambda = False

            if len(bracket) == 0:
                raise Exception(f"Lexical error on line {el['line']}: Instructions outside the brackets")

            elif check_num(cur_el):
                if is_prev_open_bracket:
                    raise Exception(f"Lexical error on line {el['line']}: Undefined lexeme '{cur_el}'")
                token = Token(el['line'], cur_index, cur_el, 'Numeric constant', str(cur_el))
                # lexemes.append([cur_index, cur_el, 'Numeric constant'])
                lexemes.append(token)
                # consts.append([cur_index, cur_el, 'Numeric constant'])
                consts.append(token)
                token_list.append(token)
                cur_index += 1
            elif check_str(cur_el):
                if is_prev_open_bracket:
                    raise Exception(f"Lexical error on line {el['line']}: Undefined lexeme '{cur_el}'")
                # lexemes.append([cur_index, cur_el, 'String constant'])
                token = Token(el['line'], cur_index, cur_el, 'String constant', str(cur_el))
                lexemes.append(token)
                # consts.append([cur_index, cur_el, 'String constant'])
                consts.append(token)
                token_list.append(token)
                cur_index += 1

            elif cur_el in KEY_WORDS.keys():
                if not is_prev_open_bracket:
                    raise Exception(f"Lexical error on line {el['line']}: Keyword is not first word '{cur_el}'")
                # lexemes.append([cur_index, cur_el, KEY_WORDS[cur_el]])
                token = Token(el['line'], cur_index, cur_el, KEY_WORDS[cur_el])
                lexemes.append(token)
                token_list.append(token)
                cur_index += 1
                if cur_el == 'LAMBDA' or cur_el == 'lambda':
                    is_prev_lambda = True
            elif cur_el in OPERATORS.keys():
                if not is_prev_open_bracket:
                    raise Exception(f"Lexical error on line {el['line']}: Operator is not first word '{cur_el}'")
                # lexemes.append([cur_index, cur_el, OPERATORS[cur_el]])
                token = Token(el['line'], cur_index, cur_el, OPERATORS[cur_el])
                lexemes.append(token)
                token_list.append(token)
                cur_index += 1
            elif check_identifier(cur_el):
                if cur_el not in [temp.text for temp in identifiers]:
                    match = check_match(cur_el, identifiers)
                    if is_prev_open_bracket:
                        raise Exception(f"Lexical error on line {el['line']}: '{cur_el}'. Do you mean using {match}?")
                    # lexemes.append([cur_index, cur_el, 'Identifier'])
                    token = Token(el['line'], cur_index, cur_el, 'Identifier')
                    lexemes.append(token)
                    # identifiers.append([cur_index, cur_el, 'Identifier'])
                    identifiers.append(token)
                    token_list.append(Token(el['line'], cur_index, cur_el, 'Identifier'))
                    cur_index += 1
                else:
                    for token in identifiers:
                        if token.text == cur_el:
                            token_list.append(Token(el['line'], token.index, token.text, token.info))
                            break
            else:
                if is_prev_open_bracket:
                    match = check_match(cur_el, identifiers)
                if is_prev_open_bracket:
                    raise Exception(f"Lexical error on line {el['line']}: '{cur_el}'. Do you mean using {match}?")
                raise Exception(f"Lexical error on line {el['line']}: {cur_el}")

            is_prev_open_bracket = False

    return lexemes, identifiers, consts, token_list


def table_output(lexemes):
    table = PrettyTable()
    table.field_names = ['id', 'identifier', 'description']
    for lex in lexemes:
        table.add_row([lex.index, lex.text, lex.info])
    return table
