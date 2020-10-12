# celsuis to fahrenheit
def cel_convert(celsuis):
    fahrenheit = (celsuis * (9/5)) + 32
    print (fahrenheit)
cel_convert(25)

# fahrenheit to celsuis
def fah_convert(fahrenheit):
    celsuis = (fahrenheit - 32) * 5/9
    print (celsuis)
fah_convert(42)
