from math import ceil


def main(y, x):
    summ = 0
    n = len(y) - 1
    for i in range(1, n + 2):
        summ += (((y[n + 1 - i]) ** 3 + 25
                  + (x[n + 1 - ceil(i / 2)]) ** 2) ** 4) / 73
    return summ


print(main([-0.29, -0.88, 0.08], [-0.26, 0.7, -0.07]))
