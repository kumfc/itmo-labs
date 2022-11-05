import re


def get_mid_frequency(f0, stp, bit_len):
    def steps_to_string(steps):
        res = ''
        for step in steps[1:]:
            if step[0] == 1:
                res += 'a'
            elif step[0] == -1:
                res += 'b'

        return res

    plt_str = steps_to_string(stp)

    length_map = dict()

    a = re.findall('(a+)', plt_str)
    b = re.findall('(b+)', plt_str)

    for substring in (a + b):
        if len(substring) in length_map:
            length_map[len(substring)] += 1
        else:
            length_map[len(substring)] = 1

    f_mid = 0
    for l, c in length_map.items():
        f_mid += f0 * c
    f_mid /= bit_len

    coefficients = sorted(length_map.items(), key=lambda k: k)

    return f_mid, coefficients
