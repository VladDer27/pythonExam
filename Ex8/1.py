import re


def main(x):
    x = x.replace("\n", '')
    x = x.replace(" ", '')
    x = x.replace("<%make", '')
    x = x.replace('"', '')
    r = r"\w+=:\w+;"
    ans = re.findall(r, x)
    keys = []
    values = []
    for i in range(len(ans)):
        ans[i] = ans[i].replace(";", '')
        ans[i] = ans[i].split("=:")
        keys.append(ans[i][1])
        values.append(ans[i][0])
    return dict(zip([data for data in keys], [data for data in values]))

print(main('|| <% make @"lesobi"=: attiar_385; %>. <% make @"ceuser"=:ononri_780;%>. <% make @"getira"=:zaeste; %>. <% make @"islele" =:onti_956; %>. ||'))