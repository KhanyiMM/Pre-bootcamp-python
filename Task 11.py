def common_letters(str1,str2):
    a = list(set(str1) & set(str2))
    for i in a:
        print(i)
common_letters('monster','summer')