


word = "faabbbcccddeeeg"

# 0. hitung jumlah karakter per huruf

# 1. how many unique character? 2 ; "fg"
# 2. hom many character with minimum duplicate three times? 3 ; bce

# mp = {}
# print(mp['f'])

def mapping(word):
    # deklarasikan dictionary kosong
    result = {}
    #iterasi/looping 'word'
    for w in word:
        # check w ada di result key-nya
        if w in result:
            # updata dictionary result bertambah 1 setiap perulangan/looping/iterasi
            result[w] = result[w] + 1
        else: 
            #klo ga ada kita isi key-pair inisial dengan angka 1
            result[w] = 1
    return result


hasil = mapping(word)

# Fungsi pendeteksi angka genap ganjil
def odd_even(num):
    if num % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")
    return None

    

odd_even(5)

def odd_even(num):
    for n in range(num):
        if n % 2 == 0:
            print(n, "Genap")
        # print(n)
        else:
            print(n, "Ganjil")
    return None

odd_even(5)

# Coder Thinking/ Computational Thinking