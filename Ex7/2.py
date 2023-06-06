def main(x):
    x = int(x, 16)
    bit_size = [2, 8, 8, 8, 5]
    m = []
    for i in range(len(bit_size)):
        m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        x = x >> bit_size[i]
    m1 = [m[2], m[4], m[3], m[0], m[1]]
    ans = 0
    ans = ans << bit_size[2]
    ans += m1[0]
    ans = ans << bit_size[4]
    ans += m1[1]
    ans = ans << bit_size[3]
    ans += m1[2]
    ans = ans << bit_size[0]
    ans += m1[3]
    ans = ans << bit_size[1]
    ans += m1[4]
    return str(hex(ans))


print(main('0x1f2ff35'))
