# i = 0
# while i<10:
#     print("hello -->", i)#i=1
#     i = i + 1
#     #i=2
       #0 1   2  3  4   5
# list = [5, 5, 6, 7, 12, 10]
# # for li in list:
# #     print(li)

# i = 0
# while i < len(list):
#     print(i)
#     i = i + 1

          #0      1    -- 2         3       4 --       5        6
# colors = ['red', 'blue','yellow', 'green', 'black', 'pink', 'yellow']
# # print(colors[2])

# # print(colors.index('yellow'))

# i = 0; c = 0
# for col in colors:
#     if col == 'yellow':
#         c = c + 1
#         if c == 3:
#             print(i)
#     i = i + 1

# some_colors = colors[2 : 5]
# print(some_colors)

# slicing from behind
# some_colors = colors[5 : 2 : -1]
# print(some_colors)

      # 0   1   2  - 3  4   5   6 -  7   8
list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# list[:] = [0,0,0]

# print(list)

# del list[3:7:2]

# print(list)

list_length = len(list)
mid = list_length//2

print(list[mid])