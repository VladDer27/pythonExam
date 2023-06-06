s = ({"YACC", 1957, 1993},
     {"YACC", 1957, 2013},
     {"YACC", 1957, 1967},
     {"YACC", 2014},
     {"GLSL", 1957, 1993},
     {"GLSL", 1957, 2013, 1971},
     {"GLSL", 1957, 2013, 2009},
     {"GLSL", 1957, 2013, 1994},
     {"GLSL", 1957, 1967, "ATS"},
     {"GLSL", 1957, 1967, "UNO"},
     {"GLSL", 2014})

def main(x):
    s1 = set(x)
    return [i for i in range(len(s))
            if not (len(s[i] - s1))][0]

print(main(['UNO', 2009, 1957, 1967, 'YACC']))