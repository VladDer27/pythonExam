def main(x):
    x = int(x, 16)
    bit_size = [4, 4, 9, 7, 2]
    m = []
    for i in range(len(bit_size)):
        if i != 3:
            m.append(int(bin(x)[2:][-bit_size[i]::], 2))
        else:
            m.append(0)
        x = x >> bit_size[i]
    ans = 0
    ans = ans << bit_size[0]
    ans += m[0]
    ans = ans << bit_size[3]
    ans += m[3]
    ans = ans << bit_size[4]
    ans += m[4]
    ans = ans << bit_size[1]
    ans += m[1]
    ans = ans << bit_size[2]
    ans += m[2]
    return ans


print(main('0x2eee87a'))
print(main('0x22c60b6'))
print(main('0x3e86ea8'))
print(main('0x2bbc631'))
