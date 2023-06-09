def main(x):
    s = ({1974, "GAP", "OZ"},
         {1974, "GAP", "FANCY"},
         {1974, "MIRAH", "OZ"},
         {1974, "MIRAH", "FANCY"},
         {1974, "RAGEL"},
         {1966, 1960, "GAP"},
         {1966, 1960, "MIRAH"},
         {1966, 1960, "RAGEL"},
         {1966, 1968},
         {2003})
    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]

print(main(['RAGEL', 1960, 2003, 'OZ']))
print(main(['MIRAH', 1968, 1966, 'FANCY']))
print(main(['GAP', 1960, 1974, 'FANCY']))
print(main(['MIRAH', 1960, 1966, 'FANCY']))
print(main(['MIRAH', 1968, 1974, 'FANCY']))