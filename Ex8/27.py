import re


def main(x):
    x = x.replace(" ", '')
    x = x.replace("\n", '')
    r = r"\w+<==\w+"
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].split("<==")
        keys.append(ans[i][0])
        values.append(ans[i][1])
    return dict(zip([data for data in keys], [data for data in values]))

print(main("( [[gean_230<== ceat_38 ]], [[ leisdi_38 <== teorbe]], )"))