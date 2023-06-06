import re


def main(x):
    x = x.replace("\n", '')
    x = x.replace(" ", '')
    x = x.replace("opt`", '')
    x = x.replace("#", '')
    r = r'\w+=array\([-?\w+,?]+\)'
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].replace(")", '')
        ans[i] = ans[i].replace("array", '')
        ans[i] = ans[i].replace("=", '')
        ans[i] = ans[i].split("(")
        keys.append(ans[i][0])
        values.append(ans[i][1])
    for i in range(len(values)):
        values[i] = values[i].split(",")
        for j in range(len(values[i])):
            values[i][j] = int(values[i][j])
    return dict(zip([data for data in keys], [data for data in values]))


print(main("<block> opt `ais_943= array( #3005 ,#-3484 ,#-4477 ) opt `tezaes_540= array(#-159 , #2342) </block>"))
