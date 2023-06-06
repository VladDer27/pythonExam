from math import log10


def main(x, z):
    ans = 77
    summ = 0
    for i in range(max(len(x), len(z))):
        summ += 86 * (log10(7 + z[i // 4] ** 2 + x[i])) ** 6
    return ans * summ

print(main([-0.96, -0.59, 0.89, 0.86, 0.38, 0.68, -0.81], [-0.97, 0.43, -0.79, -0.74, -0.76, 0.86, 0.71]))
