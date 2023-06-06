def main(x):
    s = ({2012, 1975, "PIKE"},
         {2012, 1975, "MAKO", "NIM"},
         {2012, 1975, "MAKO", "NIX"},
         {2012, 1975, "EC", 2020},
         {2012, 1975, "EC", 1981},
         {2012, 1965, "NIM", "PIKE"},
         {2012, 1965, "NIM", "MAKO"},
         {2012, 1965, "NIM", "EC"},
         {2012, 1965, "NIX", "PIKE"},
         {2012, 1965, "NIX", "MAKO"},
         {2012, 1965, "NIX", "EC"},
         {2013})
    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]

print(main([1965, 'NIX', 'MAKO', 1981, 2013]) == 11)
print(main([1975, 'NIM', 'MAKO', 1981, 2012]) == 1)
print(main([1975, 'NIM', 'PIKE', 1981, 2012]) == 0)
print(main([1965, 'NIX', 'MAKO', 2020, 2012]) == 9)
print(main([1975, 'NIX', 'EC', 2020, 2012]) == 3)