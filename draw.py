from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    dx = x1 - x0
    dy = y1 - y0
    D = 2*dy - dx
    x = x0
    y = y0

    while (x<= x1):
        plot(screen, color, x, y)
        if (D > 0):
               y = y + 1
               D = D - 2*dx
        x = x + 1
        D = D + 2*dy
