# def main(x):
#     x1 = bin(int(x['E1']))[2:].zfill(9)
#     x2 = bin(int(x['E2']))[2:].zfill(10)
#     x3 = bin(int(x['E3']))[2:].zfill(10)
#     x4 = "00000000"
#     x5 = bin(int(x['E5']))[2:].zfill(9)
#     return str(int(x5 + x4 + x3 + x2 + x1, 2))

def main(x):
    bit_size = {"E5": 9, "E4": 8, "E3": 10, "E2": 10, "E1": 9}
    ans = 0
    for i in range(len(bit_size)):
        ans = ans << int(bit_size.get("E" + str(len(bit_size) - i), 0))
        ans += int(x.get('E' + str(len(bit_size) - i), 0))
    return str(ans)


print(main({'E1': 185, 'E2': 158, 'E3': 370, 'E5': 246}))
