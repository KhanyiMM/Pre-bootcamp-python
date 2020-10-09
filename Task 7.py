# celsuis to fahrenheit
def cel_convert(x):
    celsuis = float(input('x: '))
    fahrenheit = (celsuis * (9/5)) + 32
    return (fahrenheit)
print(cel_convert(10))

# fahrenheit to celsuis
def fah_convert(z):
    fahrenheit = float(input('y: '))
    celsuis = (fahrenheit - 32) * 5/9
    return (celsuis)
print (fah_convert(9))
