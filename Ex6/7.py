def main(x):
    s = ({2000, 2015, "APL"},
         {2000, 2015, "TXL", 2005},
         {2000, 2015, "TXL", 1983},
         {2000, 2015, "GDB", 2005},
         {2000, 2015, "GDB", 1983},
         {2000, 2017, "APL", 2013},
         {2000, 2017, "APL", 1979},
         {2000, 2017, "APL", 2015},
         {2000, 2017, "TXL", 2005},
         {2000, 2017, "TXL", 1983},
         {2000, 2017, "GDB"},
         {2013})

    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]


print(main(['APL', 2000, 2017, 2005, 1979]))
print(main(['TXL', 2000, 2017, 1983, 1979]))
print(main(['GDB', 2000, 2015, 1983, 1979]))
print(main(['GDB', 2013, 2015, 1983, 2013]))
print(main(['GDB', 2000, 2017, 1983, 2015]))