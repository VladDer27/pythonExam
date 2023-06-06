import re


def main(x):
    x = x.replace(" ", '')
    x = x.replace("new@", '')
    x = x.replace("\n", '')
    x = x.replace("|", '')
    x = x.replace('"', '')
    r = "[a-z]+_?[0-9]*<list.[a-z]+_?[0-9]*;[a-z]" \
        "+_?[0-9]*;?[a-z]+_?[0-9]*;?[a-z]+_?[0-9]*."
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].replace("<list", '')
        ans[i] = ans[i].replace(")", '')
        ans[i] = ans[i].split("(")
        keys.append(ans[i][0])
        values.append((ans[i][1]))
    for i in range(len(values)):
        values[i] = values[i].split(";")
    return list(zip([data for data in keys], [data for data in values]))


print(main(
    '(|new @"soor_112" <| list(xearge; inge) | | new @"rebees_937" <| list(\nraribi ; edcere ) | | new @"axeesti" <| list(maan_917; cezaar_796 ;\norama) ||new @"enqu" <| list(angete; biqu ) |)'))
