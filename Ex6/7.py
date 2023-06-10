def main(x):
    my_dict = {2000 : {2015: {"APL": 0,
                              "TXL": {2005 : 1, 1983 : 2},
                              "GDB": {2005: 3, 1983: 4}},
                       2017: {"APL": {2013: 5, 1979: 6, 2015: 7},
                              "TXL": {2005: 8, 1983: 9},
                              "GDB": 10}},
               2013: 11}
    while isinstance(my_dict, dict):
        for s in x:
            if s in my_dict.keys():
                my_dict = my_dict[s]
                break
    return my_dict


print(main(['APL', 2000, 2017, 2005, 1979]))
print(main(['TXL', 2000, 2017, 1983, 1979]))
print(main(['GDB', 2000, 2015, 1983, 1979]))
print(main(['GDB', 2013, 2015, 1983, 2013]))
print(main(['GDB', 2000, 2017, 1983, 2015]))
