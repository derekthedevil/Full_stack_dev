class Car :
    name = "honda"
    price = 25000
    password = 123
    
    def start_car(self,password):
        if password == self.password:
            print("car is starting ..........bruuuummmmmm")
        else :
            print("access denied ! please enter correct password")

Car()
c1 = Car()
print(c1.name)
print(c1.price)
c1.start_car(256)
c1.start_car(123)
# The 4 pillars of OOP in Python:

# 1. Encapsulation - Bundling data and methods that operate on that data within a single unit
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private variable with double underscore
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance

# Example of encapsulation
account = BankAccount()
account.deposit(1000)
print("\nEncapsulation example:")
print(f"Balance: {account.get_balance()}")  # Accessing private variable through public method

# 2. Inheritance - Ability of a class to inherit attributes and methods from another class
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Example of inheritance
print("\nInheritance example:")
dog = Dog("Max")
print(dog.speak())

# 3. Polymorphism - Same interface for different forms (data types/classes)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

def animal_sound(animal):
    print(animal.speak())

# Example of polymorphism
print("\nPolymorphism example:")
dog = Dog("Max")
cat = Cat("Whiskers")
animal_sound(dog)
animal_sound(cat)

# 4. Abstraction - Hiding complex implementation details and showing only necessary features
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass





class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width

# Example of abstraction
print("\nAbstraction example:")
rect = Rectangle(5, 3)
print(f"Rectangle area: {rect.area()}")

