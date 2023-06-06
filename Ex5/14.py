from math import tan, ceil


def main(y, x, z):
    summ = 0
    n = len(x) - 1
    for i in range(1, n + 2):
        summ += 49 * tan(29 * (y[i - 1]) ** 2 -
                         26 * (z[n + 1 - ceil(i / 2)]) ** 3 - x[i - 1]) ** 5

    return summ


print(main([0.61, 0.42, -0.69, 0.96, -0.26], [0.49, -0.93, -0.02, -0.52, 0.85], [0.31, 0.66, -0.46, 0.55, -0.1]))
