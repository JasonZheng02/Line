from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    A = y1 - y0
    B = (x1 - x0) * -1
    x = x0
    y = y0
    slope = (A / B) * -1

    if (slope < 1 and slope > 0):
        D = 2*A + B
        while (x<= x1):
            plot(screen, color, x, y)
            if (D > 0):
                   y = y + 1
                   D = D + 2 * B
            x = x + 1
            D = D + 2 * A
