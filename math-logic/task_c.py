from plex.parser import parse, Node
from core.impl_checker import *
from core.lemmas import *


def main():
    hypotheses_list, statement = parse(input())
    glivenko = f"{', '.join(hypotheses_list)} |- {Node('!', Node('!', statement))}".strip()
    expressions = []
    statement = str(statement)

    line = ''
    while line != statement:
        line = str(parse(input()))
        expressions.append(line)

    proof = []
    for i in range(len(expressions)):
        expr = expressions[i]
        is_mp, v1, v2 = is_modus_ponens(expressions, expr, i)
        is_ax10, v = is_tenth_axiom(expr)
        if is_hypo(hypotheses_list, expr) or (not is_mp and not is_ax10):
            proof += get_main_proof(expr)
        elif is_ax10:
            proof += get_axiom10_proof(v)
        elif is_mp:
            proof += get_modus_ponens_proof(v1, v2)

    print(glivenko)
    print('\r\n'.join(proof))


if __name__ == '__main__':
    main()
