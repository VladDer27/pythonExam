import re


def main(x):
    x = x.replace(" ", '')
    x = x.replace("\n", '')
    x = x.replace("#", '')
    x = x.replace("dostoreq", '')
    r = r"\(\w+\)islist\([-?\w+,?]+\)"
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].replace("(", '')
        ans[i] = ans[i].replace(")", '')
        ans[i] = ans[i].split("islist")
        keys.append(ans[i][0])
        values.append(ans[i][1])
    for i in range(len(values)):
        values[i] = values[i].split(",")
        for j in range(len(values[i])):
            values[i][j] = int(values[i][j])
    return list(zip([data for data in keys], [data for data in values]))


print(main(
    "<section>do store q(riesge)is list( #-9261,#-4531 , #3866 , #-2539 )done. do store q(iszaan) is list( #-3448 ,#-6377 ,#413) done. do storeq(anonbe) is list( #7384 ,#7796) done. do store q(anerza_406)islist(#1772,#-1155, #-8174 , #9175 )done. </section>"))
