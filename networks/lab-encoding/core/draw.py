import matplotlib.pyplot as plt


class Visualizer:
    def __init__(self, line_color, text_color, line_width):
        self.line_color = line_color
        self.text_color = text_color
        self.line_width = line_width

    def draw_code(self, bits, steps, levels = 3):
        x = [steps[0][1]]
        y = [steps[0][0]]
        cur = steps[0][1]

        for i in range(1, len(steps)):
            cur += steps[i][1]

            x.append(x[-1])
            y.append(steps[i][0])
            x.append(cur)
            y.append(steps[i][0])

        f = plt.figure()
        f.set_figwidth(10)
        f.set_figheight(0.7 * levels)

        ticks = [i - (levels // 2) for i in range(levels)]
        lim = (levels - 1 - levels // 2)

        ax = f.add_subplot(1, 1, 1)
        ax.set_xticks([i for i in range(len(bits))])
        ax.set_yticks(ticks)
        ax.grid(which='both')

        plt.plot(x, y, linewidth=self.line_width, color=self.line_color)
        plt.tick_params(axis='both', which='both', top=False, bottom=False, labelbottom=False, right=False, left=False,
                        labelleft=False)
        for i in range(len(bits)):
            plt.text(i + 0.4, lim + 0.15, bits[i], color=self.text_color)

        plt.ylim([-lim - 0.2 * lim, lim + 0.45])
        plt.xlim([0, len(bits)])
        plt.show()
