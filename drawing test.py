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


def draw_golden_rectangle(pad: ImageDraw, x, y, length, direction="horizontal",
                          color="black", n=0, n_max=4, m=0, m_max=0):
    print((x, y, length, direction, color, n, n_max, m, m_max))
    if n >= n_max:
        return  # enough iterations
    width = length / GOLDEN_RATIO

    if direction == "vertical":
        points = [(x, y), (x + width, y),
                  (x + width, y + length), (x, y + length)]
        print(points)

        # next iteration
        n += 1
        x = x
        y = y + width
        length = width
        direction = "vertical" if direction == "horizontal" else "horizontal"
        draw_golden_rectangle(pad, x, y, length, direction=direction, color=color_generator_random(color),
                              n=n, n_max=n_max, m=m, m_max=m_max)
    else:
        points = [(x, y), (x + length, y),
                  (x + length, y + width), (x, y + width)]
        print(points)

        # next iteration
        n += 1
        x = x
        y = y
        length = width
        direction = "vertical" if direction == "horizontal" else "horizontal"
        draw_golden_rectangle(pad, x, y, length, direction=direction, color=color_generator_random(color),
                              n=n, n_max=n_max, m=m, m_max=m_max)

    pad.polygon(points, fill=color)


def color_generator_bw(color):
    return "black" if color == "white" else "white"


def color_generator_random(*args, **kwargs):
    return '{:02x}{:02x}{:02x}'.format(*np.random.choice(range(256), size=3))

img, idraw = create_canvas()

draw_golden_rectangle(idraw, MARGIN, MARGIN, LENGTH - 2 * MARGIN, color=color_generator_random(), n_max=2)

img.save('golden_fractal.jpg')

img.show()

