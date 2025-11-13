# Exercise 9: OOP – Class and Inheritance
#
# Test your understanding of object-oriented programming principles with this multi-part challenge.
#
# Base Class
# Define a base class Vehicle with attributes make and model
#
# Inheritance
# Create a subclass Car that adds an attribute num_doors
#
# Method
# Write a method in Car to display all attributes

class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self,make,model,num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    def display_attributes(self):
        print(f"The vehicle manufacturer is {self.make}")
        print(f"The vehicle model is {self.model}")
        print(f"The num of doors to vehicle is {self.num_doors}")

toyota = Car("Toyota","Corolla",5)
toyota.display_attributes()

super_car = toyota(num_doors = 2)
super_car.display_attributes()