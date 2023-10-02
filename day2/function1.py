# #function adalah fungsi/kumpulan perintah untuk komputer yang dibungkus dengan keyword def dan diakhiri 
# # dengan ":" serta diikuti dengan indentasi/spasi yang bisa memiliki balikan(return) maupun tidak 


# #Function tanpa balikan(return)
# def myFunctionHello():
#     print("Hello")

# def sayHelloName(name):
#     print("Hello Mr/Ms", name)


# myFunctionHello()

# sayHelloName("Fajri")

# #Function dengan balikan(return)
# def myFunctionHelloWithBalikanOrReturn():
#     return "Hello with return"

# #Trigger
# response = myFunctionHelloWithBalikanOrReturn()
# print(response)


# def add(num1, num2):
#     return num1 + num2

# result = add(3, 4) # Output : 7
# print(result)
# print(add(1, 5)) #Output : 6

# Quiz 
# Function Pengurangan
# def substract(parameter1, parameter2):
#     print()
#     print(
#         "Pengurangan parameter1=" \
#         + str(parameter1) \
#         + " dikurang parameter2=" \
#         + str(parameter2) \
#         + " adalah " \
#         + str(parameter1 - parameter2)
#         )
#     print()

# Function Perkalian
# def multiply(argument1, argument2):
#     print('Perkalian arguments adalah ' + str(argument1 * argument2))

# # substract(100, 20)
# multiply(3, 4)

def alat_pendeteksi_kategori_golongan_usia(input):
    #Jika usia subjek 0 - 17 tahun, maka subjek adalah 'Anak Kecil'
    if input > 0 and input < 18:
        print ("\nSubject Anak Kecil!\n") 
    #Jika usia subjek 18 - 60 tahun, maka subjek adalah 'Dewasa'
    elif input >=18 and input < 60:
        print ("\nSubject Dewasa!\n")
    #Jika usia subjek diatas 60 tahun, maka subjek adalah 'Lansia'
    elif input > 60 and input < 100:
        print ("\nSubject Lansia!\n")
    #Jika usia di bawah 0 atau bilangan bulat negative, maka 'Salah Input!'
    else:
        print ("\n\n\nSalah input atau usia tidak mungkin di atas 100 tahun!\n\n\n") #\n -> new line -> baris baru

input_interaksi_terminal = input('Masukkan usia : ') #prompt
alat_pendeteksi_kategori_golongan_usia(int(input_interaksi_terminal))

# Intermezzo JAVA
# class Function1 {
#     public static String alatPendeteksiGolongan(Integer input) {
#         Integer a = 10;
#         Integer b = 5;
#         result = a + b + input;
#         return result;
#     }
# }

