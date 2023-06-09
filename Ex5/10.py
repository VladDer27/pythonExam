from math import ceil


def main(x):
    ans = 0
    n = len(x)
    for i in range(1, n + 1):
        ans += (6 * x[n - ceil(i / 3)] ** 2 - 58 * x[n - i] ** 3 - 36) ** 7
    return ans


print(main([0.89, -0.67, 0.79, 0.61, -0.15]))
print(main([-0.31, -0.67, 0.93, 0.91, -0.16]))
print(main([-0.85, -0.6, 0.13, 0.52, 0.18]))
print(main([0.52, 0.93, -0.35, 0.17, -0.98]))
print(main([0.33, -0.07, 0.33, 0.21, -0.18]))
