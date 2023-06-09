import re


def main(x):
    x = x.replace("\n", '')
    x = x.replace(" ", '')
    x = x.replace("<:((", '')
    x = x.replace("))", '')
    x = x.replace("new", '')
    r = r"\w+<==\w+"
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].split("<==")
        keys.append(ans[i][0])
        values.append(ans[i][1])
    return list(zip([data for data in keys], [data for data in values]))

print(main("<: (( new laus <== ceve )) (( new isla_100 <== edan_477 )) (( newusenbi<== onis_718 )) (( new atle_324 <== raaran_892 )) :>"))