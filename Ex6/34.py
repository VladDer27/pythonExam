def main(x):
    # my_dict = {"DYLAN" : {"NUMPY" : {"BRO" : 0, "QML" : 1, "ROUGE" : 2},
    #                       "HYPHY" : {"PAWN" : 3, "AMPL" : 4},
    #                       "EDN" : 5},
    #            "HAXE" : 6,
    #            "CSS" : {"PANW": {"NUMPY" : 7, "HYPHY" : 8, "EDN" : 9},
    #                     "AMPL": 10}}
    # while isinstance(my_dict, dict):
    #     for i in x:
    #         if i in my_dict.keys():
    #             my_dict = my_dict[i]
    #             break
    # return my_dict
    s = ({"DYLAN", "NUMPY", "BRO"},
         {"DYLAN", "NUMPY", "QML"},
         {"DYLAN", "NUMPY", "ROUGE"},
         {"DYLAN", "HYPHY", "PAWN"},
         {"DYLAN", "HYPHY", "AMPL"},
         {"DYLAN", "EDN"},
         {"HAXE"},
         {"CSS", "PAWN", "NUMPY"},
         {"CSS", "PAWN", "HYPHY"},
         {"CSS", "PAWN", "EDN"},
         {"CSS", "AMPL"})
    s1 = set(x)
    return [i for i in range(len(s))
            if not len(s[i] - s1)][0]

print(main(['PAWN', 'NUMPY', 'HAXE', 'QML']))
print(main(['PAWN', 'HYPHY', 'CSS', 'QML']))
print(main(['PAWN', 'HYPHY', 'DYLAN', 'ROUGE']))
print(main(['PAWN', 'EDN', 'CSS', 'ROUGE']))
print(main(['AMPL', 'EDN', 'CSS', 'QML']))