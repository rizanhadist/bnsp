
# Class/blueprint
class Vehicle:
    # constructor/init
    def __init__(self, name):
        self.name = name
        
    # methods
    def maju(self, wheel):
        print("Brrrmmmmmm.........Majuuuu --->" + self.name + str(wheel))
    def mundur(self):
        print("Ngeeeeng............Muhnduur")


# mobil = Vehicle("BMW")

# mobil.maju(3)
# mobil.mundur()

class Car(Vehicle):
    #class Car extends Vehicle {} (Java)
    def __init__(self, name, door):
        super().__init__(name)
        self.door =door
        
    
    def open_door(self):
        print("Open the door ---> ", self.door)

# class MotorCycle(Vehicle):
#     def __init__(self, wheel):
#         super().__init__(wheel)

bmw = Car("bmw", 4)
bmw.maju(2)
bmw.open_door()


tuple_data = (1, 3, 5)
