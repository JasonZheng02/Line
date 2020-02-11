from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    if (x0 > x1):
        x0, x1 = x1, x0
    if (y0 > y1):
        y0, y1 = y1, y0
    A = y1 - y0
    B = (x1 - x0) * -1
    x = x0
    y = y0
    slope = (A / B) * -1
    print(slope)

    if (slope <= 1 and slope > 0):
        D = 2*A + B
        while (x<= x1):
            plot(screen, color, x, y)
            if (D > 0):
                y = y + 1
                D = D + 2 * B
            x = x + 1
            D = D + 2 * A

    if (slope > 1):
        D = A + 2 * B
        while (y<= y1):
            plot(screen, color, x, y)
            if (D < 0):
                x = x + 1
                D = D + 2 * A
            y = y + 1
            D = D + 2 * B

    if (slope < -1):
        D = A + 2 * B
        while (y<= y1):
            plot(screen, color, x, y)
            if (D < 0):
                x = x - 1
                D = D + 2 * A
            y = y + 1
            D = D + 2 * B
