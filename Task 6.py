def max_number(number): 
    max = numbers[0] 
    for x in numbers: 
        if x > max : 
             max = x    
    return max
numbers = [73,32,10,156,201] 
print(max_number(numbers))