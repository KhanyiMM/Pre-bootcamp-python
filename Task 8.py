def time_convert(x):
    x = int(input('x: '))
    minutes = x % 60
    hours = x / 60
    if x >= 2:
        return (hours)
    else x =< 2:
        return (minutes)
print(hours + 'hours' + " ," + minutes + 'minutes')