def main(x):
    x = int(x, 16)
    bit_size = [2, 7, 1, 8]
    m = []
    for i in range(len(bit_size)):
        m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        x = x >> bit_size[i]
    ans = 0
    ans = ans << bit_size[0]
    ans += m[0]
    ans = ans << bit_size[2]
    ans += m[2]
    ans = ans << bit_size[1]
    ans += m[1]
    ans = ans << bit_size[3]
    ans += m[3]
    return str(hex(ans))


print(main('0x57bc'))
