from core.utils import longest_repetitive_bit


def redundant_encode(msg):
    table = {
        '0000': '11110',
        '0001': '01001',
        '0010': '10100',
        '0011': '10101',
        '0100': '01010',
        '0101': '01011',
        '0110': '01110',
        '0111': '01111',
        '1000': '10010',
        '1001': '10011',
        '1010': '10110',
        '1011': '10111',
        '1100': '11010',
        '1101': '11011',
        '1110': '11100',
        '1111': '11101'
    }
    enc = ''
    for i in range(0, len(msg), 4):
        enc += table[msg[i:i + 4]]

    return enc


def scramble(a, b, msg):
    res = msg[:a]
    for i in range(a, len(msg)):
        bit = int(msg[i]) ^ int(res[i - a])
        if i - b >= 0:
            bit ^= int(res[i - b])
        res += str(bit)

    return res


def scramble_best(msg):
    poly_list = [(3, 5), (5, 7), (3, 7)]
    shortest = longest_repetitive_bit(msg)
    print('[Scramble]  Input', shortest)
    best = (None, msg)

    for poly in poly_list:
        new_msg = scramble(*poly, msg)
        l = longest_repetitive_bit(new_msg)
        print('[Scramble] ', poly, l)
        if l < shortest:
            shortest = l
            best = (poly, new_msg)

    return best
