def time_convert(x):
    minutes = x % 60
    hours = x // 60
    print(hours, "hours,", minutes, "minutes")
time_convert(432)