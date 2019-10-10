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


def generate_golden_rectangle(pad: ImageDraw, x, y, length, direction=0, m_max=4):

    width = length / GOLDEN_RATIO
    square = [(x, y), (x + width, y), (x + width, y + width), (x, y + width), (x, y)]
    rect = []
    if direction == 0:
        upleft = square[1]
        rect = [upleft,
                translate_point(*upleft, length - width, 0),
                translate_point(*upleft, length - width, width),
                translate_point(*upleft, 0, width),
                upleft]
    elif direction == 1:
        upleft = square[3]
        rect = [upleft,
                translate_point(*upleft, width, 0),
                translate_point(*upleft, width, length - width),
                translate_point(*upleft, 0, length - width),
                upleft]
    return square, rect


def recursive_golden_rectangle(pad, x, y, length, n=0, n_max=4, color="black", direction=0, m_max=4, arch_dir=1):
    if n >= n_max:
        return
    n += 1

    # base
    square, rect = generate_golden_rectangle(pad, x, y, length, direction=direction)
    pad.line(square, fill=color, width=5)
    pad.line(rect, fill=color, width=5)

    archimedes_spiral(pad, square, m=0, m_max=m_max)

    # recursion
    recursive_golden_rectangle(pad, *rect[0], length / GOLDEN_RATIO, direction=(direction + 1) % 2,
                               n=n, n_max=n_max, color=color_generator_bw(color), m_max=m_max, arch_dir=-1*arch_dir)


def archimedes_spiral(pad, points, m=0, m_max=4, ratio=GOLDEN_RATIO, color='black'):
    # points must include 5 points including closure
    if m >= m_max:
        return

    #shift = (x2 - x1)/GOLDEN_RATIO

    new_points = []
    for i in range(0, 4):
        (x1, y1) = points[i]
        (x2, y2) = points[i+1]
        new_points.append((x1 + (x2 - x1)/GOLDEN_RATIO, y1 + (y2 - y1)/GOLDEN_RATIO))
    new_points.append(new_points[0])
    pad.line(points, fill=color, width=5)

    m += 1
    archimedes_spiral(pad, new_points, m, m_max, ratio, color)


def draw_circle(pad, center, radius):
    x, y = center
    pad.arc([x-radius, y-radius, x+radius, y+radius], 0, 360, fill="red", width=20)


def translate_point(x, y, tx, ty):
    return x + tx, y + ty


def translate(points, tx, ty):
    return [translate_point(x, y, tx, ty) for (x, y) in points]


def color_generator_bw(color):
    return "blue" if color == "black" else "black"


def color_generator_random(*args, **kwargs):
    return '#{:02x}{:02x}{:02x}'.format(*np.random.choice(range(256), size=3))


def main():
    img, idraw = create_canvas()
    length = LENGTH - 2 * MARGIN
    margin = MARGIN
    recursive_golden_rectangle(idraw, margin, margin, length, color='black', n_max=10, m_max=20, arch_dir=1)

    img.save('golden_fractal.jpg')

    img.show()

main()
