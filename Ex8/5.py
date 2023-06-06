import re


def main(x):
    x = x.replace("\n", '')
    x = x.replace(" ", '')
    x = x.replace(".beginauto", '')
    r = r"-?[0-9]+to[a-z]+_?[0-9]*"
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].split("to")
        keys.append(ans[i][1])
        values.append(ans[i][0])
    return dict(zip([data for data in keys], [int(data) for data in values]))


print(main("(( .begin auto 6023 to abi_276. .end. .begin auto -7450 to iscela_703..end. ))"))
