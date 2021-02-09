import ply.yacc as yacc
from plex.lexer import tokens

precedence = (
    ('right', 'IMPLIES'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NEG')
)


class Node:
    def __init__(self, act, parts):
        self.act = act
        self.parts = parts

    def __repr__A(self):
        if self.act == 'var':
            return str(self.parts)
        elif self.act == '!':
            return f'(!{self.parts})'
        else:
            return f'({self.act},{self.parts[0]},{self.parts[1]})'

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.act == 'var':
            return str(self.parts)
        elif self.act == '!':
            return f'!{self.parts}'
        else:
            return f'({self.parts[0]} {self.act} {self.parts[1]})'


def p_line(p):
    '''
    line : proof_header
         | expression
    '''

    p[0] = p[1]


def p_proof_header(p):
    '''
    proof_header : BAZAR expression
                 | context BAZAR expression
    '''

    if len(p) == 3:
        p[0] = ([], p[2])
    else:
        p[0] = (p[1], p[3])


def p_context(p):
    '''
    context : expression
            | context COMMA expression
    '''

    if len(p) == 2:
        p[0] = [str(p[1])]
    else:
        p[1].append(str(p[3]))
        p[0] = p[1]


def p_expression(p):
    '''
    expression : VAR
               | LQ expression RQ
               | NEG expression
               | expression AND expression
               | expression OR expression
               | expression IMPLIES expression
    '''

    p_len = len(p)
    if p_len == 2:
        p[0] = Node('var', p[1])
    elif p_len == 3:
        p[0] = Node('!', p[2])
    elif p_len == 4 and p[1] == '(':
        p[0] = Node('var', p[2])
    elif p_len == 4:
        p[0] = Node(p[2], (p[1], p[3]))


def p_error(p):
    print(f'Unexpected token: {p}')


parser = yacc.yacc(debug=0, write_tables=0)


def parse(code):
    return parser.parse(code)
