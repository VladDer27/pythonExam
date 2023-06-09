from math import ceil


def main(z, y, x):
    ans = 0
    n = len(z)
    for i in range(1, n + 1):
        ans += 14 * abs(95 * x[ceil(i / 3) - 1] + z[n - ceil(i / 2)] ** 2 + 19 * y[i - 1] ** 3) / 15
    return ans


print(main([0.92, -0.24],
           [-0.54, 0.16],
           [0.92, 0.19]))
