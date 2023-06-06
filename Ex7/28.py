def main(x):
    bit_size = [10, 7, 6, 5, 10]
    ans = 0
    for i in range(len(bit_size)):
        ans = ans << bit_size[i]
        if i != 2:
            ans += x['G' + str(len(bit_size) - i)]
    return ans


print(main({'G1': 968, 'G2': 12, 'G4': 118, 'G5': 181}))
