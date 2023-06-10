def main(x):
    x = int(x, 16)
    bit_size = [3, 5, 3, 9, 7, 2]
    m = []
    ans = 0
    for i in range(len(bit_size)):
        if i != 4:
            m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        else:
            m.append(0)
        x = x >> bit_size[i]
    ans = ans << bit_size[1]
    ans += m[1]
    ans = ans << bit_size[5]
    ans += m[5]
    ans = ans << bit_size[4]
    ans += m[4]
    ans = ans << bit_size[0]
    ans += m[0]
    ans = ans << bit_size[3]
    ans += m[3]
    ans = ans << bit_size[2]
    ans += m[2]
    return ans

print(main('0x19ff9bd7'))
print(main('0xfe970a8'))
print(main('0xaa5dfeb'))
print(main('0x39adbf4'))