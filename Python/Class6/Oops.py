# OOPs: --> Object oriented programmings

    # Class
    # Object
    # Inheritance
    # Polymorphism
    # Abstraction

# Class
    # Example 1:
        # class Car:
        #     no_wheels = 0
        #     no_sheets = 0
        #     color = ""
        #     fuel = ""

        #     def car_speed(self):
        #         print("This car speed is: ", 280)

        # honda = Car()

        # honda.no_wheels = 5
        # honda.no_sheets = 7
        # honda.color = "Black"
        # honda.fuel = "Petrol"

        # print(honda.color)

        # i10 = Car()

        # i10.no_wheels = 4
        # i10.no_sheets = 5
        # i10.color = "silver"
        # i10.fuel = "Disel"

        # print(i10.color)

        # honda.car_speed()
        # i10.car_speed()

    # Example 2:

        # class Car:
        #     def __init__(self, wheels, sheets, colors, fuels):
        #         self.no_wheels = wheels
        #         self.no_sheets = sheets
        #         self.color = colors
        #         self.fuel = fuels

        #     def car_speed(self):
        #         print("This car speed is: ", 280)

        # honda = Car(5, 7, "Black","Petrol")
        # hyundai = Car(4, 5, "Red", "Disel")
        # Volvo = Car(6, 6, "white", "EV")

        # print(honda.fuel)
        # print(honda.color)

        # print("---------------------------")

        # print(hyundai.fuel)
        # print(hyundai.color)

        # print("---------------------------")

        # print(Volvo.fuel)
        # print(Volvo.color)