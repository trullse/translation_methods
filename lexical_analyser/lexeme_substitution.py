from token import Token


def lexeme_substitution(token_list, identifiers_info, consts_info):
    for token in token_list:
        raw_lex = token.text
        done = False
        for info in identifiers_info:
            if info.text == raw_lex:
                token.text = '<id' + str(info.index) + '>'
                done = True
                break
        if not done:
            for info in consts_info:
                if info.text == raw_lex:
                    token.text = '<id' + str(info.index) + '>'
                    done = True
                    break
    return token_list
