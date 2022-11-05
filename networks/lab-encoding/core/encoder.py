from core.utils import bin_to_hex
from core.phys_encoders import *
from core.logic_encoders import *
from copy import deepcopy


phys_enc_dict = {
    'manchester': Manchester,
    'nrz': NRZ,
    'rz': RZ,
    'ami': AMI,
    'nrzi': NRZI,
    'manchester-diff': ManchesterDiff,
    'mlt-3': MLT3,
    'pam-5': PAM5
}


class BitString:
    def __init__(self, message):
        self.message = message

    @property
    def message_hex(self):
        return bin_to_hex(self.message)

    @property
    def bit_len(self):
        return len(self.message)

    @property
    def byte_len(self):
        return len(self.message) / 8

    def lab_repr(self, ceil = True):
        print('HEX:', self.message_hex)
        print('BIN:', self.message)
        print()
        if ceil:
            print(int(self.byte_len), 'байт')
        else:
            print(self.byte_len, 'байт')
        print(self.bit_len, 'бит')


class MessageEncoder(BitString):
    def __init__(self, msg: str, bandwidth, vis: Visualizer, bits_to_vis=32, encoding='cp1251'):
        message = ''.join([f'{i:08b}' for i in msg.encode(encoding)])
        self.C = bandwidth
        self.vis = vis
        self.vis_len = bits_to_vis

        super().__init__(message)

    def update_message(self, msg):
        self.message = msg

    def phys_encode(self, code_type):
        return phys_enc_dict[code_type](self.message[:self.vis_len], self.C, self.vis)

    def redundant_logic_encoder(self):
        enc = redundant_encode(self.message)
        ret = deepcopy(self)
        ret.update_message(enc)
        return ret

    def scramble(self, poly: tuple = None):
        if poly:
            enc = scramble(poly[0], poly[1], self.message)
        else:
            poly, enc = scramble_best(self.message)

        ret = deepcopy(self)
        ret.update_message(enc)
        return poly, ret
