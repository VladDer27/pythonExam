def main(x):
    l1 = "000000000"
    l2 = bin(int(x["L2"]))[2:].zfill(1)
    l3 = bin(int(x["L3"]))[2:].zfill(5)
    l4 = bin(int(x["L4"]))[2:].zfill(5)
    l5 = bin(int(x["L5"]))[2:].zfill(9)
    l6 = bin(int(x["L6"]))[2:].zfill(7)
    return int(l6 + l5 + l4 + l3 + l2 + l1, 2)

print(main({'L2': '0', 'L3': '20', 'L4': '18', 'L5': '509', 'L6': '34'}))