def lexeme_thread_maker(raw_lexemes, identifiers_info, consts_info):
    identifiers = [sublist[0] for sublist in identifiers_info]
    lexeme_thread = ''

    for raw_lex_info in raw_lexemes:
        raw_lex = raw_lex_info['lexeme']
        done = False
        for info in identifiers_info:
            if info[1] == raw_lex:
                lexeme_thread += '<id' + str(info[0]) + '>'
                done = True
                break
        if not done:
            for info in consts_info:
                if info[1] == raw_lex:
                    lexeme_thread += '<id' + str(info[0]) + '>'
                    done = True
                    break
        if not done:
            lexeme_thread += raw_lex
    return lexeme_thread
