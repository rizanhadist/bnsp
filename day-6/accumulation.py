def accumulate(*params):
    sum = 0
    for param in params:
        sum = sum + param
    print(sum)

accumulate(3,2,1)