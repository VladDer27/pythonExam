import re


def main(x):
    x = x.replace("begin define", '')
    x = x.replace("{{", '')
    x = x.replace("}}", '')
    x = x.replace(" ", '')
    x = x.replace("\n", '')
    r = r"[a-z]+_?[0-9]*==>[a-z]+_?[0-9]*"
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].split("==>")
        keys.append(ans[i][1])
        values.append(ans[i][0])
    return dict(zip([data for data in keys], [data for data in values]))


print(main(
    "{{begin define teave ==> usqued_62; end, begin define teace_736 ==> era_405; end, begin define maraat ==>reso; end, begin define vege_200==> onin;end, }}"))
