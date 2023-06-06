s = ({1976, 1984, "TEXT"},
     {1976, 1984, "TCSH"},
     {1976, 2001},
     {1965, 1984, "TEXT"},
     {1965, 1984, "TCSH"},
     {1965, 2001, "GLSL"},
     {1965, 2001, "ABAP"},
     {1996, 1984, "GLSL"},
     {1996, 1984, "ABAP"},
     {1996, 2001, "TEXT"},
     {1996, 2001, "TCSH"})


def main(x):
    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]
