def main(x):
    x = int(x)
    bit_size = [4, 1, 10, 8]
    m = []
    for i in range(len(bit_size)):
        m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        x = x >> bit_size[i]
    return [hex(m[i]) for i in range(len(m))]


print(main("3029662"))
print(main("4945707"))
print(main("5599789"))
print(main("5141984"))
