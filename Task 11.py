def common_letters(str1,str2):
    str1=input("x: ")
    str2=input("y: ")
    a= list(set(str1) & set(str2))
    for i in a:
        print(i)
common_letters('hello','bongiwe')