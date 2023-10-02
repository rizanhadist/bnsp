import sys

print(sys.maxsize, len('9223372036854775807'))

def min_value(*args):
    min = sys.maxsize
    for arg in args:
        if arg < min:
            min = arg
        # print(arg)
    print(min)


min_value(100,2,3,4,-4)