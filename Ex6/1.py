def main(x):
    s = ({1999, "NL", "COOL"},
         {1999, "NL", "MAX"},
         {1999, "CLEAN", "COOL"},
         {1999, "CLEAN", "MAX"},
         {1971, "NL", 2009},
         {1971, "NL", 1985},
         {1971, "CLEAN", 2009},
         {1971, "CLEAN", 1985},
         {1983, 2009, "NL"},
         {1983, 2009, "CLEAN"},
         {1983, 1985})

    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]


print(main([1983, 2009, 'CLEAN', 'COOL']))
print(main([1983, 1985, 'NL', 'MAX']))
print(main([1971, 1985, 'NL', 'COOL']))
print(main([1983, 2009, 'NL', 'COOL']))
print(main([1971, 2009, 'CLEAN', 'MAX']))