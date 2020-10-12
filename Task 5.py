def triangle(x,y,z):
    s = (x + y + z) / 2
    area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
    print (area)
triangle(9,10,11)