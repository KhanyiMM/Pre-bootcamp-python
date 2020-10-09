def three(x,y):
    if x == 3 or y == 3:
        return True
    elif (x + y).contains('3'):
        return True
    else:
        return False
print(three(3,0))
print(three(7,3))
print(int(three(7,6)))