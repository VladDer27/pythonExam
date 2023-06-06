def main(x):
    x = int(x)
    bit_size = [6, 10, 10, 1]
    m = []
    for i in range(len(bit_size)):
        m.append(int(bin(x)[2:][-bit_size[len(bit_size) - 1 - i]::], 2))
        x = x >> bit_size[len(bit_size) - 1 - i]
    return tuple([str(m[i]) for i in range(len(m)) if i != 2])

print(main('121956816'))