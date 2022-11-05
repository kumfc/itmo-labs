import re


def longest_repetitive_bit(s):
    return max(max(len(a), len(b)) for a, b in re.findall('(0+)?(1+)?', s))


def bin_to_hex(s):
    ret = []
    for i in range(0, len(s), 8):
        ret.append(f'{int(s[i:i + 8], 2):02x}')

    return ' '.join(ret).upper()