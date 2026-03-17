# Inheritance

class GrandFather:
    isHaveAssets = True

    def car_speed(self):
        print("My car speed is: ", 280)

class Parent(GrandFather):

    def __init__(self, amt):
        self.bankBalance = 500000
        self.savings = amt

    def bikeColor(self):
        print("My Bike color is: ", "Blue")

class Child(Parent):
    pocketMoney = 500

    def __init__(self, amt):
        super().__init__(amt)


son = Child(100)

print(son.bankBalance)
print(son.savings)