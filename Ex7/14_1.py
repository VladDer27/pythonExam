def main(x):
    bit_size = [9, 1, 5, 5, 9, 7]
    m = [0]
    for i in range(1, len(bit_size)):
        m.append(x.get('L' + str(i + 1)))
    ans = 0
    for i in range(len(bit_size) - 1, - 1, -1):
        ans = ans << bit_size[i]
        ans += int(m[i])
    return ans


print(main({'L2': '0', 'L3': '20', 'L4': '18', 'L5': '509', 'L6': '34'}))
print(main({'L2': '1', 'L3': '10', 'L4': '3', 'L5': '464', 'L6': '107'}))
print(main({'L2': '0', 'L3': '3', 'L4': '9', 'L5': '281', 'L6': '94'}))
print(main({'L2': '1', 'L3': '16', 'L4': '30', 'L5': '282', 'L6': '62'}))
