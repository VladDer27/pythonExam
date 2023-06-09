def main(x):
    bit_size = [10, 1, 4, 10, 4, 1]
    m = []
    for i in range(len(bit_size)):
        m.append(x[i][1])
    ans = 0
    for i in range(len(m) - 1, -1, -1):
        ans = ans << bit_size[i]
        ans += int(m[i], 16)
    return hex(ans)


print(main([('A1', '0x2bc'), ('A2', '0x0'), ('A3', '0x2'), ('A4', '0x146'), ('A5', '0x0'), ('A6', '0x0')]))
print(main([('A1', '0x103'), ('A2', '0x1'), ('A3', '0x6'), ('A4', '0x54'), ('A5', '0xc'), ('A6', '0x0')]))
print(main([('A1', '0x365'), ('A2', '0x0'), ('A3', '0x6'), ('A4', '0x350'), ('A5', '0xb'), ('A6', '0x1')]))
print(main([('A1', '0x277'), ('A2', '0x1'), ('A3', '0x6'), ('A4', '0x34f'), ('A5', '0x7'), ('A6', '0x1')]))
