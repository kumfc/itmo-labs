from core.draw import Visualizer
from core.mid_frequency import get_mid_frequency


class PhysEncoder:
    f_high_div = 1
    f_low_div = 1
    f_mid_div = 1
    levels = 3

    def __init__(self, string: str, bandwidth, vis: Visualizer):
        self.f_high = 0
        self.f_low = 0
        self.f_mid = 0
        self.s = 0
        self.f_mid_cf = list()

        self.string = string
        self.vis = vis
        self.C = bandwidth

        self.steps = self.encode(string)
        self.calc_frequency()

    def draw(self):
        self.vis.draw_code(self.string, self.steps, self.levels)

    def calc_frequency(self):
        self.f_high = self.C / self.f_high_div
        self.f_low = self.C / self.f_low_div
        self.f_mid, self.f_mid_cf = get_mid_frequency(self.f_high, self.steps, len(self.string) * self.f_mid_div)
        self.s = 7 * self.f_high - self.f_low

    def lab_repr(self):
        f_mid_upper_seg = ' + '.join([f'({e[0] * e[1]} / {e[0]})*f0' for e in self.f_mid_cf])
        print()
        print(f'f_high = {self.C} / {self.f_high_div} = {self.f_high} MHz')
        print(f'f_low = {self.C} / {self.f_low_div} = {self.f_low} MHz')
        print(f'f_mid = ({f_mid_upper_seg}) / {len(self.string) * self.f_mid_div} = {self.f_mid} MHz')
        print(f'S = 7 * {self.f_high} - {self.f_low} = {self.s} MHz')
        print()

    def encode(self, bits):
        pass


class NRZ(PhysEncoder):
    f_high_div = 2
    f_low_div = 6
    f_mid_div = 1

    def encode(self, bits):
        steps = [[1, 0] if bits[0] == '1' else [-1, 0]]
        for bit in bits:
            steps.append([1, 1]) if bit == '1' else steps.append([-1, 1])

        return steps


class RZ(PhysEncoder):
    f_high_div = 1
    f_low_div = 4
    f_mid_div = 1

    def encode(self, bits):
        steps = [[1, 0] if bits[0] == '1' else [-1, 0]]
        for bit in bits:
            steps.append([1, 0.5] if bit == '1' else [-1, 0.5])
            steps.append([0, 0.5])

        return steps


class AMI(PhysEncoder):
    f_high_div = 2
    f_low_div = 8
    f_mid_div = 1

    def encode(self, bits):
        steps = [[1, 0] if bits[0] == '1' else [0, 0]]
        up = True
        for bit in bits:
            if bit == '1':
                steps.append([1, 1]) if up else steps.append([-1, 1])
                up = not up
            else:
                steps.append([0, 1])

        return steps


class NRZI(PhysEncoder):
    f_high_div = 2
    f_low_div = 4
    f_mid_div = 1

    def encode(self, bits):
        steps = [[1, 0] if bits[0] == '1' else [-1, 0]]
        up = False
        for bit in bits:
            if bit == '1':
                up = not up
            steps.append([1, 1] if up else [-1, 1])

        return steps


class Manchester(PhysEncoder):
    f_high_div = 1
    f_low_div = 2
    f_mid_div = 2

    def encode(self, bits):
        steps = [[-1, 0] if bits[0] == '1' else [1, 0]]
        for bit in bits:
            if bit == '1':
                steps.append([-1, 0.5])
                steps.append([1, 0.5])
            else:
                steps.append([1, 0.5])
                steps.append([-1, 0.5])

        return steps


class ManchesterDiff(PhysEncoder):
    f_high_div = 1
    f_low_div = 2
    f_mid_div = 2

    def encode(self, bits):
        steps = [[1, 0] if bits[0] == '1' else [-1, 0]]
        for bit in bits:
            if bit == '1':
                steps.append([steps[-1][0], 0.5])
                steps.append([-steps[-2][0], 0.5])
            else:
                steps.append([-steps[-1][0], 0.5])
                steps.append([steps[-2][0], 0.5])

        return steps


class MLT3(PhysEncoder):
    f_high_div = 2
    f_low_div = 10
    f_mid_div = 1

    def encode(self, bits):
        steps = [[0, 0]]
        h = 0
        up = True
        for bit in bits:
            if bit == '1':
                if h == 0:
                    h = 1 if up else -1
                else:
                    up = not up
                    h = 0
            steps.append([h, 1])

        return steps


class PAM5(PhysEncoder):
    levels = 5

    def encode(self, bits):
        steps = [[0, 0]]
        for i in range(0, len(bits), 2):
            if bits[i:i+2] == '00':
                steps.append([-2, 2])
            elif bits[i:i+2] == '01':
                steps.append([-1, 2])
            elif bits[i:i+2] == '10':
                steps.append([1, 2])
            else:
                steps.append([2, 2])

        return steps

    def calc_frequency(self):
        pass

    def lab_repr(self):
        raise NotImplementedError
