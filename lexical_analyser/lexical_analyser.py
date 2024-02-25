from tkinter import filedialog as fd
from .lexemes_identifier import lexemes_identifier, table_output
from .lexeme_divider import lexeme_divider
from .lexeme_thread_maker import lexeme_thread_maker
from .lexeme_substitution import lexeme_substitution


def lexical_analyser(code, output=False):
    raw_lexemes = lexeme_divider(code)
    try:
        lexemes, identifiers, consts, tokens = lexemes_identifier(raw_lexemes)
    except Exception as e:
        print(e)
        return
    table = table_output(lexemes)
    if output:
        print(table)
    # lexeme_thread = lexeme_thread_maker(raw_lexemes, identifiers, consts)
    # print(lexeme_thread)
    tokens_subst = lexeme_substitution(tokens, identifiers, consts)
    if output:
        print(''.join([token.text for token in tokens_subst]))
    return tokens_subst


if __name__ == "__main__":
    filename = fd.askopenfilename(filetypes=(('txt files', '*.txt'),))
    with open(filename, "r") as f:
        code = f.read()
    lexical_analyser(code, True)

