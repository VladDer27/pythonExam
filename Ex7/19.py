def main(x):
    x = int(x, 16)
    m = []
    bit_size = [1, 8, 3, 9, 9]
    for i in range(len(bit_size)):
        if i != 4:
            m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        else:
            m.append(0)
        x = x >> bit_size[i]
    return dict(zip(["Q" + str(i + 1) for i in range(len(m))], [hex(m[i]) for i in range(len(m)) if i != 4]))


print(main("0x4e484"))
print(main("0x14c0df"))
print(main("0x19f3c8"))
print(main("0x1a0436"))
