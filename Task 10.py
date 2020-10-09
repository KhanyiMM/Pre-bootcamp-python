def find_vowels(word):
    word = input('x: ')
    for word in word:
        if word in 'aeiouAEIOU':
            print (word)
find_vowels('hello')