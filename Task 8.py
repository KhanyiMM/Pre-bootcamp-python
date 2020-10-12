def time_convert():
    x = int(input('x: '))
    minutes = x % 60
    hours = x // 60
    print(hours, "hours,", minutes, "minutes")
time_convert()