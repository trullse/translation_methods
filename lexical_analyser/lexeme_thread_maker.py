from token import Token


def lexeme_thread_maker(raw_lexemes, identifiers_info, consts_info):
    identifiers = [sublist.text for sublist in identifiers_info]
    lexeme_thread = ''

    for raw_lex_info in raw_lexemes:
        raw_lex = raw_lex_info['lexeme']
        done = False
        for info in identifiers_info:
            if info.text == raw_lex:
                lexeme_thread += '<id' + str(info.index) + '>'
                done = True
                break
        if not done:
            for info in consts_info:
                if info.text == raw_lex:
                    lexeme_thread += '<id' + str(info.index) + '>'
                    done = True
                    break
        if not done:
            lexeme_thread += raw_lex
    return lexeme_thread
