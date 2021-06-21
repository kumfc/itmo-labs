import ply.lex as lex

tokens = [
    'NUMBER',
    'HEADER',
    'EQUATION',
    'UNDERCUT',
    'S',
    'Y'
]

t_NUMBER = r'-?[0-9]+(?:\.[0-9]+)?'
t_HEADER = r'\[s[1-4]\]'
t_EQUATION = r'='
t_UNDERCUT = r'_'
t_S = r's[1-4]'
t_Y = 'y'

t_ignore = '\t\x20\r\n'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
