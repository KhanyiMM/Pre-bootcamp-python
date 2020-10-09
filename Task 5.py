def triangle(x,y,z):
    x = float(input('x: '))
    y = float(input('y: '))
    z = float(input('z: '))
    s = (x + y + z) / 2
    area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
    return (area)
print (triangle(7,8,9))