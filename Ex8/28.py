import re


def main(x):
    x = x.replace("\n", '')
    x = x.replace('"', '')
    x = x.replace(" ", '')
    r = r"[a-z]+_?[0-9]*=#-?[0-9]+"
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].split("=#")
        keys.append(ans[i][0])
        values.append(ans[i][1])
    return dict(zip([data for data in keys], [int(data) for data in values]))


print(main('\\begin || decl @"anarer" = #9981;|||| decl @"gebequ_198" =\n#-4218;||||decl @"xeedza_504"= #8633; || || decl @"maus_673" = #6939;\n||\\end'))
