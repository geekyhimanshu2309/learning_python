# Polymorphism - It allows objects of different classes to be treated as objects of a common super class. It enables code reusability and flexibility, making programs more scalable and maintainable.

# Types of polymorphism: Python supports polymorphism in multiple ways
# 1. Method overriding (Rutime polymorphism)
# 2. Method overloading (Compile-time polymorphism)
# 3. Operator overloading
# 4. Duck Typing

# Method Overriding: When a subclass provides a specific implementation of a method that is already defined in parent class.
# Example: 
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Creating objects of different subclasses
animals = [Dog(), Cat(), Animal()]

# Polymorphic behavior
for animal in animals:
    print(animal.speak())  

# Method Overloading: Python does not support true method overloading (like Java or CPP), but it can be simulated using default parameters or variable-length arguments

class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

math = MathOperations()
print(math.add(5, 10))      # Calls method with two arguments
print(math.add(5, 10, 15))  # Calls method with three arguments

# Operator Overloading: Python allows operators like +,-,*,/ etc, to be overloaded using special methods (dunder methods)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2  # Calls __add__ method
print(p3)  # Output: (6, 8)

# Duck Typing(Dynamic Polymorphism): Duck typing allows us to use objects of different classes interchangeably, as long as they have the required methods.

class Bird:
    def fly(self):
        return "Bird is flying"

class Airplane:
    def fly(self):
        return "Airplane is flying"

def make_it_fly(obj):
    print(obj.fly())

make_it_fly(Bird())      # Output: Bird is flying
make_it_fly(Airplane())  # Output: Airplane is flying

