from Expression import *
from postfix import parsePostfix
import math
import pygame

pygame.init()

def map(value, from_min, from_max, to_min, to_max):
    return to_min + (to_max-to_min) * (value-from_min) / (from_max-from_min)

def calculateFunctionDataset(expr: Expression, min_x: float, max_x: float, width: int, height: int):
    data = []
    for pos_x in range(width):
        x = map(pos_x, 0, width-1, min_x, max_x)
        data.append((x, float(expr({"x": map(pos_x, 0, width-1, min_x, max_x)}))))
    maximum = 0
    for item in data:
        maximum = max(maximum, abs(item[1]))
    ratio = height/2/maximum
    for pos in range(width):
        data[pos] = (data[pos][0], data[pos][1] * ratio)
    return data

def renderFunction(expr: Expression, min_x: float, max_x: float, width: int, height: int):
    data = calculateFunctionDataset(expr, min_x, max_x, width, height)
    surface = pygame.display.set_mode((width, height))
    surface.fill((40, 42, 54))
    best = (0, 100000)
    for x in range(width):
        number = abs(data[x][0])
        if number < best[1]:
            best = (x, number)
    half_height = height/2
    pygame.draw.line(surface, (0xbd, 0x93, 0xf9), (best[0], 0), (best[0], height))
    pygame.draw.line(surface, (0xbd, 0x93, 0xf9), (0, half_height), (width, half_height))
    for x in range(width):
        pygame.draw.rect(surface, (0x39,0xed,0x7b), (x, -data[x][1]+half_height, 1, 1))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
    pygame.display.quit()

def main():
    (expr, _) = parsePostfix("|x|+1")
    renderFunction(expr, -50, 50, 1920, 1080)
    # result = calculateFunctionDataset(expr, -10, 10, 21, 15)
    # for val in result:
    #     print(val)

if __name__ == "__main__": main()
