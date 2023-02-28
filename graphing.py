from Expression import *
from postfix import parsePostfix
import math

def map(value, from_min, from_max, to_min, to_max):
    return to_min + (to_max-to_min) * (value-from_min) / (from_max-from_min)

def calculateDataset(expr: Expression, min_x: float, max_x: float, width: int, height: int):
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

def main():
    (expr, _) = parsePostfix("(x)(x)(x)")
    result = calculateDataset(expr, 0, 10, 21, 15)
    for val in result:
        print(val)

if __name__ == "__main__": main()
