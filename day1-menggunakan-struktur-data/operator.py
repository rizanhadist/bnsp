import math

a = 1
b = 2


# print(math.ceil(10.4))
# print('a + b =', a + b)
# print('a - b =', a - b)
# print('a * b =', a * b)
# print('a / b =', a / b)
# print('a // b =', a // b)
# print('a modulus b =', a % b)
# print('a ** b =', a**b)

# ctrl + /
# print('a > b ', a > b)
# print('a < b ', a < b)
# print('a == b', a == b)
# print('a != b', a == b)
# print('a >= b ', a >= b)


# print(True and True) # True
# print(True and False) #False
# print(False and True) #False
# print(False and False) #False

# print(True or True) # True
# print(True or False) #True
# print(False or True) #True
# print(False or False) #False

# print(not True)
# x = "fajri"
# # y = x is 5
# print(x is "fajri")

# a = "My name is Fajri"
# print("Fajri" in a)
# b = [1,2,3,4,5]
# print(1 in b)
# dictionary = {"name" : "Fajri", 1:"mantap"}
# print("Name" in  dictionary)

x = 5
x &= 9 # x = x | 9 ---> 5 | 9

print(5^9)

# 1 = 0 0 0 0 1 -----> (0)(2^4) + (0)(2^3) + (0)(2^2) + (0)(2^1) + (1)(2^0) ------> 0(16) + 0(8) + 0(4) + 0(2) + 1(1) ----> 0 + 0 + 0 + 0 + 1 ----> 1
# 2 = 0 0 0 1 0
# 3 = 0 0 0 1 1
# 4 = 00100

# 5 = 00101
# 9 = 01001
# 5 | 9 = 01101 ---> (0)(2^4) + (1)(2^3) + (1)(2^2) + (0)(2^1) + (1)(2^0) = 13
# 5 & 9 = 00001 = 1
# 5 ^ 9 = 01100 = 12