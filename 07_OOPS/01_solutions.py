# Basic Class and Object
# Problem1: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car: 
  def __init__ (self, userbrand, usermodel):                # Self is same as this, both have same meanings and known as context for linkage
    self.brand = userbrand
    self.model = usermodel

  def fullName (self):
    return f"{self.brand} {self.model}"

my_car = Car("Toyota","Corola")

print(my_car.brand,my_car.model)

# Problem2: Add a method to the Car class that displays the full name of the car(brand and model)
print(my_car.fullName())
