from PIL import Image, ImageDraw, ImageColor
import numpy as np

MARGIN = 50  # make sure we can print on a normal margin printer
LENGTH = 297*10
WIDTH = 210*10


GOLDEN_RATIO = (1 + 5 ** 0.5) / 2


def create_canvas():
    img = Image.new('RGB', (LENGTH, WIDTH), 'white')
    idraw = ImageDraw.Draw(img)

    return img, idraw


def generate_golden_rectangle(pad: ImageDraw, x, y, length, m_max=4):

    width = length / GOLDEN_RATIO
    square = [(x, y), (x + width, y), (x + width, y + width), (x, y + width), (x, y)]
    rect = [(x + width, y), (x + length, y), (x + length, y + width), (x, y + width), (x, y)]

    return square, rect


def recursive_golden_rectangle(pad, x, y, length, n=0, n_max=4, color="black"):
    if n >= n_max:
        return
    n += 1

    print((x, y, length, n, n_max, color))

    # base
    square, rect = generate_golden_rectangle(pad, x, y, length)
    pad.line(square, fill=color, width=5)
    pad.line(rect, fill=color, width=5)

    # recursion
    recursive_golden_rectangle(pad, x, y, length / GOLDEN_RATIO, n=n, n_max=n_max, color=color_generator_bw(color))


def archimedes_spiral(pad, points, m=0, m_max=4, ratio=GOLDEN_RATIO, color='black'):
    # points must include 5 points including closure
    if m >= m_max:
        return

    tx, ty = points[0]

    new_points = []
    for i in range(0, 4):
        (x1, y1) = points[i]
        (x2, y2) = points[i+1]
        new_points.append((x1 + (x2 - x1)/GOLDEN_RATIO, y1 + (y2 - y1)/GOLDEN_RATIO))
    new_points.append(new_points[0])
    pad.line(points, fill=color, width=5)

    m += 1
    archimedes_spiral(pad, new_points, m, m_max, ratio, color)


def translate(points, tx, ty):
    return [(x - tx, y - ty) for (x, y) in points]


def rotate(points, degrees):
    pass


def color_generator_bw(color):
    return "blue" if color == "black" else "black"


def color_generator_random(*args, **kwargs):
    return '#{:02x}{:02x}{:02x}'.format(*np.random.choice(range(256), size=3))


def main():
    img, idraw = create_canvas()
    length = 1000  # LENGTH - 2 * MARGIN
    width = length / GOLDEN_RATIO
    margin = 600
    recursive_golden_rectangle(idraw, margin, margin, length, color='black', n_max=10)

    initial_square = [(1500, 1500), (1500, 2000), (2000, 2000), (2000, 1500), (1500, 1500)]
    #archimedes_spiral(idraw, initial_square, m_max=10)

    img.save('golden_fractal.jpg')

    img.show()

main()
