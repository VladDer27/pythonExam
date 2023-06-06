import re


def main(x):
    x = x.replace("\n", '')
    x = x.replace(" ", '')
    x = x.replace("|", '')
    x = x.replace("eginstorelist", '')
    x = x.replace("#", '')
    x = x.replace("\\end", '')
    r = r"\([-?\w+;?]+\)>`\w+;"
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].replace(">`", '')
        ans[i] = ans[i].replace("(", '')
        ans[i] = ans[i].split(")")
        keys.append(ans[i][1])
        values.append(ans[i][0])
    for i in range(len(values)):
        values[i] = values[i].split(";")
        for j in range(len(values[i])):
            values[i][j] = int(values[i][j])
    for i in range(len(keys)):
        keys[i] = keys[i].replace(";", '')
    return list(zip([data for data in keys], [data for data in values]))


print(main(
    "| \begin store list(#3137;#2423; #-6401 ) |> `usa_510; \end. \beginstore list( #8399 ; #818 ; #-1021 ;#-6543 ) |> `anedbe_887;\end.\beginstore list(#-6916; #9659 ) |> `lear_434;\end.|"))
