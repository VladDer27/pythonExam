def main(x):
    bitsize = [10, 8, 10, 8]
    m = []
    for i in range(len(bitsize)):
        if i != 2:
            m.append(int(bin(x)[2:][-bitsize[i]::], 2))
        else:
            m.append(0)
        x = x >> bitsize[i]
    ans = 0
    ans = ans << bitsize[3]
    ans += m[3]
    ans = ans << bitsize[0]
    ans += m[0]
    ans = ans << bitsize[2]
    ans += m[2]
    ans = ans << bitsize[1]
    ans += m[1]
    return str(hex(ans))


print(main(16345819042))
