def main(x):
    x = int(x, 16)
    bitsize = [4, 2, 6, 1, 7, 9]
    m = []
    for i in range(len(bitsize)):
        m.append(int(bin(x)[2:][-bitsize[i]::], 2))
        x = x >> bitsize[i]
    return dict(zip(['C' + str(i + 1) for i in range(len(m))],
                    [str(m[i]) for i in range(len(m))]))


print(main('0x1693883d'))
