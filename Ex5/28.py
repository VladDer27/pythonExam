from math import ceil, floor


def main(x):
    summ = 0
    n = len(x) - 1
    for i in range(1, n + 2):
        summ += 60 * floor(0.03 - 86 * (x[n + 1 - ceil(i / 2)]) ** 2
                           - x[n + 1 - ceil(i / 2)]) ** 4
    return summ


print(main([-0.01, -0.54, -0.24]))
