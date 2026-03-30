# Polymorphism:

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak() 
        print("Dog barks: Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat meows: Meow! Meow!")

# Polymorphism in action
animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()