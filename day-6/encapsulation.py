# Encapsulation (dikapsulkan / disembunyikan)
class Account:
    # state (constructor +  attribute)
    def __init__(self, name, birth_of_date, cc_number) -> None:
        self.name = name
        #private
        self.__birth_of_date = birth_of_date
        self.cc_number = cc_number
    #setter/ getter
    def get_birth_of_date(self):
        return (self.__birth_of_date)
    def set_birth_of_date(self, set_birth_of_date):
        self.__birth_of_date = set_birth_of_date

account1 = Account("Fajri", "12/12/12", "12345678")


print(account1.name)
print(account1.get_birth_of_date())
print(account1.cc_number)
account1.set_birth_of_date("13/13/13")
print(account1.get_birth_of_date())

