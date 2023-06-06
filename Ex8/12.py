import re


def main(x):
    x = x.replace("\n", '')
    x = x.replace(" ", '')
    x = x.replace("{{", '')
    x = x.replace("#", '')
    x = x.replace('"', '')
    r = r"-?[0-9]+to\w+;"
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].replace(";", '')
        ans[i] = ans[i].split("to")
        keys.append(ans[i][1])
        values.append(ans[i][0])
    return dict(zip([data for data in keys], [int(data) for data in values]))


print(
    main('\begin {{ #2706 to "eren_708"; }}. {{#529 to"tiso";}}. {{#771to"beso_623";}}.{{#-2384 to "leaus"; }}. \end"'))
