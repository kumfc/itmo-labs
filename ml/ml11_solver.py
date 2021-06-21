import ply.yacc as yacc
from ml11_lexer import tokens
import z3

eq_builder = None


class VvelGovno(Exception):
    pass


class EquationBuilder:
    def __init__(self, y):
        self.y = y
        self.equations = z3.Solver()
        self.sc = {'s1': z3.Real('s1'), 's2': z3.Real('s2'),
                   's3': z3.Real('s3'), 's4': z3.Real('s4')}

    def add_equation(self, s, params):
        equation = []
        for i in range(len(params[0])):
            pi = params[0][i]
            equation.append([pi, []])
            for P in params[1 + i * 2]:
                equation[-1][1].append([P])
            for j in range(len(params[1 + i * 2])):
                equation[-1][1][j].append(params[2 + i * 2][j])

        self.equations.add(eval(self.__eq_to_str(s, equation)))

    def __eq_to_str(self, s, eq):
        string = f'self.sc["{s}"] == ('
        for v in eq:
            string += f'+{v[0]}*('
            for sub in v[1]:
                string += f'+{sub[0][1]}*({sub[1]}+{self.y}*self.sc["{sub[0][0]}"])'
            string += ')'
        string += ')'

        return string

    def solve(self):
        if self.equations.check() == z3.sat:
            print(f'Поеш!')
            m = self.equations.model()
            print(sorted([(d, eval(str(m[d]))) for d in m], key=lambda x: str(x[0])))
        else:
            raise VvelGovno('Чел ты ввел говно система не решается....')


def p_all(p):
    '''
    all : yheader block block block block
    '''

    p[0] = p[1]


def p_yheader(p):
    '''
    yheader : Y EQUATION NUMBER
    '''

    global eq_builder
    eq_builder = EquationBuilder(p[3])

    p[0] = p[3]


def p_block(p):
    '''
    block : HEADER numeric line_move numeric
          | HEADER numeric line_move numeric line_move numeric
    '''

    global eq_builder
    eq_builder.add_equation(p[1][1:-1], p[2::])

    p[0] = p[1::]


def p_move(p):
    '''
    move : S UNDERCUT NUMBER
    '''

    p[0] = (p[1], p[3])


def p_line_move(p):
    '''
    line_move : move
              | move move
              | move move move
    '''

    p[0] = p[1::]


def p_numeric(p):
    '''
    numeric : NUMBER
            | NUMBER NUMBER
            | NUMBER NUMBER NUMBER
    '''

    p[0] = p[1::]


def p_error(p):
    print(f'Unexpected token: {p}')


parser = yacc.yacc(debug=0, write_tables=0)


def parse(code):
    parser.parse(code)


def main():
    global eq_builder
    with open('example.txt') as f:
        parse(f.read())
    eq_builder.solve()


if __name__ == '__main__':
    main()
