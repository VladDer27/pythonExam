def main(x):
    s = ({"XOJO", "MQL4", "LATTE", 1987},
         {"XOJO", "MQL4", "LATTE", 2005},
         {"XOJO", "MQL4", "GLYPH", 1987},
         {"XOJO", "MQL4", "GLYPH", 2005},
         {"XOJO", "MQL4", "SELF", "C++"},
         {"XOJO", "MQL4", "SELF", "ARC"},
         {"XOJO", "STAN"},
         {"XOJO", "SLASH"},
         {"TOML", 1987, "C++"},
         {"TOML", 1987, "ARC", "LATTE"},
         {"TOML", 1987, "ARC", "GLYPH"},
         {"TOML", 1987, "ARC", "SELF"},
         {"TOML", 2005},
         {"SHELL"})
    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]


print(main(['XOJO', 'SELF', 2005, 'MQL4', 'C++']))
print(main(['SHELL', 'SELF', 2005, 'STAN', 'C++']))
print(main(['TOML', 'SELF', 1987, 'SLASH', 'ARC']))
print(main(['TOML', 'LATTE', 2005, 'STAN', 'ARC']))
print(main(['XOJO', 'LATTE', 2005, 'MQL4', 'ARC']))
