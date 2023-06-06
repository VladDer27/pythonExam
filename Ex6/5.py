s = ({"EQ", 1990, "PAWN"},
     {"EQ", 1990, "RUBY"},
     {"EQ", 1990, "COBOL"},
     {"EQ", 1981, 1976},
     {"EQ", 1981, 1989},
     {"EQ", 1981, 2012},
     {"EQ", 1998, 1976},
     {"EQ", 1998, 1989},
     {"EQ", 1998, 2012},
     {"HACK"},
     {"XOJO"})


def main(x):
    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]


print(main(['EQ', 1976, 1981, 'COBOL']))
