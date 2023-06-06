s = ({1982, "ORG", 2005, "CSON"},
     {1982, "ORG", 2005, "JAVA"},
     {1982, "ORG", 2005, "MIRAH"},
     {1982, "ORG", 1993},
     {1982, "ORG", 1997, "HACK"},
     {1982, "ORG", 1997, "EDN"},
     {1982, "ORG", 1997, "VUE"},
     {1982, "C++"},
     {1982, "NINJA"},
     {1979})


def main(x):
    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]
