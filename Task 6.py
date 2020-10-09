def max_number(array): 
    max = array[0] 
    for x in array: 
        if x > max : 
             max = x    
    return max

array = [73,32,10,156,201] 
print(max_number(array)) 