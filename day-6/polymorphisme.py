# Polymorphisme(banyak bentuk) -> Override dan Overload
class Burung:

    def __init__(self) -> None:
        pass

    def terbang(self):
        print("wuzzz wuzzzz ...")

# Override -> nama method sama, tipe data balikan sama, parameter sama
class BurungMerpati(Burung):
    def __init__(self) -> None:
        pass
    def terbang(self):
        print("wozzz wozzzz....")

# Overload -> nama method sama, tipe data balikan sama, parameter beda
class BurungKakaTua(Burung):
    def __init__(self) -> None:
        pass

    def terbang(self, talk):
        print("fuzzz fuzzz...", talk)


#instantiate to be object
burung = Burung()
merpati1 = BurungMerpati()
kaka_tua1 = BurungKakaTua()

burung.terbang()
merpati1.terbang()
kaka_tua1.terbang("Burung kakak tua!, Burung kakak tua!")