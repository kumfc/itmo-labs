def is_modus_ponens(expressions, expr, index):
    expressions_slice = expressions[:index]
    for expression in expressions_slice:
        if f'({expression} -> {expr})' in expressions:
            return True, expression, expr
    return False, None, None


def is_hypo(hypotheses_list, expr):
    return expr in hypotheses_list


def is_tenth_axiom(expr):
    b = expr[3:-1]
    mid = len(b)//2
    return b[:mid - 2] == b[mid + 2:] and expr[:3] == '(!!' and b[mid - 2:mid + 2] == ' -> ', b[:mid - 2]
