def main(x):
    s = ({1981, 2003, 1973},
         {1981, 2003, 2012, "TOML"},
         {1981, 2003, 2012, "M4"},
         {1981, 2003, 2012, "HACK"},
         {1981, 2003, 1990, "TOML"},
         {1981, 2003, 1990, "M4"},
         {1981, 2003, 1990, "HACK"},
         {1981, 1959},
         {1981, 1976, "TOML"},
         {1981, 1976, "M4"},
         {1981, 1976, "HACK"},
         {2011})
    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]


print(main([2012, 'TOML', 1976, 'LESS', 1981]))
print(main([1990, 'M4', 1976, 'LESS', 2011]))
print(main([1973, 'HACK', 1959, 'PLSQL', 1981]))
print(main([1973, 'TOML', 2003, 'PLSQL', 1981]))
print(main([1990, 'M4', 2003, 'PLSQL', 1981]))
