def three(x,y):
    total_sum = x + y
    if '3' in str(total_sum):
        return True
    elif x == 3 or y == 3:
        return True
    else:
        return False
print(three(7,8))