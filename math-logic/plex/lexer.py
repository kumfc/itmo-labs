import ply.lex as lex

tokens = [
    'VAR',
    'LQ',
    'RQ',
    'NEG',
    'AND',
    'OR',
    'IMPLIES',
    'COMMA',
    'BAZAR'
]

t_VAR = r'[A-Z](?:[A-Z0-9\']+)?'
t_LQ = r'\('
t_RQ = r'\)'
t_NEG = r'!'
t_AND = r'&'
t_OR = r'\|'
t_IMPLIES = r'->'
t_COMMA = r','
t_BAZAR = r'\|-'

t_ignore = '\t\x20\r'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
