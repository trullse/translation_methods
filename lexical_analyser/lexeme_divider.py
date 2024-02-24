def lexeme_divider(code: str):
    lexemes = []
    is_comment = False
    is_string = False
    cur_lexeme = ''
    cur_line = 1

    for sym in code:
        if is_comment:
            if sym == '\n':
                is_comment = False

        elif is_string:
            if sym == '"':
                is_string = False
                cur_lexeme += sym
                lexemes.append({'line': cur_line, 'lexeme': cur_lexeme})
                cur_lexeme = ''
            else:
                cur_lexeme += sym

        elif sym == '"' and not is_comment:
            is_string = True
            cur_lexeme += sym

        elif sym == ';':
            is_comment = True
            if len(cur_lexeme) != 0:
                lexemes.append({'line': cur_line, 'lexeme': cur_lexeme})
                cur_lexeme = ''

        elif sym in ('(', ')'):
            if len(cur_lexeme) != 0:
                lexemes.append({'line': cur_line, 'lexeme': cur_lexeme})
                cur_lexeme = ''
                is_string = False
            lexemes.append({'line': cur_line, 'lexeme': sym})

        elif sym.isspace():
            if len(cur_lexeme) != 0:
                lexemes.append({'line': cur_line, 'lexeme': cur_lexeme})
                cur_lexeme = ''
            if sym == '\n':
                cur_line += 1

        else:
            cur_lexeme += sym

    return lexemes