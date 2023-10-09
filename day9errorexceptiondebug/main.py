# import requests

# data = [0, 1, 2, 3]
# print(data[6])

# data = {
#     'name': 'Fajri',
#     'address': 'Riau',
#     'leg': 3
# }

# print(data['name'])
# print(data['eye'])

# try:
#     data = 'Fajri'
#     print(dataa)
# except:
#     print("Error is happening!!!")

# randomList = ['a', 0, 2]

# try:
#     print(randomList[10])
# except:
#     print("Danger!!! It is error!!!")

randomList = [1, 2, 3]
try:
    print(randomList[5])
except Exception as e:
    print('Some error')
    print(e)
