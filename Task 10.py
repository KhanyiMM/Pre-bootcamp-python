def find_vowels(str1):
    str1 = input('x: ')
    for a in str1:
        if a in 'aeiouAEIOU':
            print (a)
find_vowels('hello')