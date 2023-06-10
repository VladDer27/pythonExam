def main(x):
    my_dict = {2002 : {"DIFF" : {2014: {"M": 0, "NL": 1, "COBOL": 2},
                                 1994: {"M": 3, "NL": 4, "COBOL": 5}},
                       "LFE": 6,
                       "KRL": 7},
               1976: {"DIFF": {2014: 8, 1994: 9},
                      "LFE": 10,
                      "KRL": 11},
               1963: 12}
    while isinstance(my_dict, dict):
        for s in x:
            if s in my_dict.keys():
                my_dict = my_dict[s]
                break
    return my_dict

print(main([1994, 'NL', 'LFE', 1970, 2002]))
print(main([2014, 'M', 'KRL', 2007, 1963]))
print(main([2014, 'NL', 'KRL', 2007, 1976]))
print(main([2014, 'COBOL', 'LFE', 1970, 1976]))
print(main([2014, 'M', 'DIFF', 2007, 2002]))