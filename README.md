# golden_ratio_fractal_art
Just having fun with the Golden Ratio and Archimedes's spiral

It's a script, just run in Python 3.5+

It is made to proportions of an A4 page and there are some high level parameters:
MARGIN = 50  # make sure we can print on a normal margin printer
LENGTH = 297*10
WIDTH = 210*10
THICKNESS = 2

To play with the patterns:
recursive_golden_rectangle(idraw, margin, margin, length, color='black', n_max=15, m_max=20, arch_dir=0)
n_max is the number of "Golden Rectangles"
m_max is the number of fractal iterations in each square generated

To remove the spiral, just comment line 60: draw_circle(pad, square[(2+direction) % 4], width, 180 + direction*90, 270 + direction*90)


Of course it could be made interactive etc., but the goal here was just to have fun and print a "mathematical mozaic pattern"
for an art workshop.

Feel free to use!
