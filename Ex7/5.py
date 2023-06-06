def main(x):
    bit_size = [3, 5, 9, 7, 2]
    m = []
    for i in range(len(bit_size)):
        m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        x = x >> bit_size[i]
    return [('M' + str(1 + i), m[i]) for i in range(len(m)) if i != 2]

print(main(61424733))
