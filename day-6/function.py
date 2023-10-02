import sys

# def test(a=10, b=2):
#     return a*b

# print(test(30, 5))

# Menghitung rata-rata
def calculate_avg(list):
    sum = 0
    for element in list:
        sum = sum + element

    return sum/len(list)

# Menghitung rata-rata
def calculate_avg(list):
    return sum(list)/len(list)

print(calculate_avg([1,2,3,4,5]))

# leetcode.com (buat latihan algoritma/coding)

# Fungsi menghitung nilai terbesar dari list (built in)
def max_number(list):
    return max(list)

# Fungsi menghitung nilai terbesar dari list (native)
def max_number(list):
    max = - sys.maxsize - 1
    for i in range(len(list)-1):
        if list[i] < list[i+1]:
            max = list[i+1]
    return max

print(max_number([1,3,6,1,2,3]))
