
# # class
# class Mammal:
#     # constructor
#     def __init__(self, rahim, kelenjar_susu, anak):
#         self.rahim = rahim
#         self.kelenjar_susu = kelenjar_susu
#         self.anak = anak
    
#     def melahirkan(self, jumlah):
#         print(f'Beranak sebanyak {jumlah}')
#         self.anak = self.anak + jumlah

# #instatiate supaya jadi object paus dari class Mammal
# paus = Mammal(1, 2, 10)

# #OOP terjadi ketika implemantasi class, attribute, method, dan object tercapai kalau di python.

# print(paus.anak)

# paus.melahirkan(5)
# print(paus.anak)


class Human:

    def __init__(self, health=100, energi=100):
        self.health=health
        self.energi=energi


    def dipukul(self, energi):

        print("Gedebug!!!")
        if self.health == 0 :
            print(f"Gabisa dikurangin lagi bos!!! -------------> {self.health}")
        print(f"Health awal akan dikurangi {energi}")
        self.health = self.health - energi
        if self.health < 0 :
            print("Game Over!!!")
            self.health = 0
            print(f"Sudah koid Bos! -------------> {self.health}")
        else:
            print(f"Health berkurang menjadi {self.health}")
    

fajri = Human()
fajri.dipukul(60)
fajri.dipukul(50)
fajri.dipukul(10)
fajri.dipukul(50)
fajri.dipukul(10)
print(fajri.health)