# __init__ is a constructor here

# What is a constructor?
# A constructor in python is a special method named __init__ that is automatically called when a new object of a class is created.
# It is used to initialize an object's attributes
# class ClassName:
    # def __init__(self, parameters):
        # Initialization code

class Person:
    def __init__(self, name, age):  # Constructor
        self.name = name  # Initializing instance variables
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object
person1 = Person("Alice", 25)

print(person1.greet())  # Output: Hello, my name is Alice and I am 25 years old.

# KEY POINTS
# - The constructor is defined using __init__ (self,...)
# - "self" represents the instance of the class and allows access to its attributes
# - The constructor is automatically called or invoked when an object is created
# - It is used to initialize attributes with default or user-provided values.
# NOTE: If a class does not define __init__, Python provides a default constructor that does nothing.

# When to use a constructor?
# - When you need to initialize instance attributes at the time of object creation
# - When you want to enforce certain required parameters of an object
# - When setting up default values for object properties


# 1. When you need to initialize instance attributes at the Time of object creation

# Example: Initializing Attributes at object creation

class Car:
    def __init__(self, brand, model):
        self.brand = brand                  # Instance Attributes
        self.model = model                  # Instance Attributes

    def details(self):
        return f"This car is a {self.brand} {self.model}"
    
# Creating objects with specific attributes
car1 = Car("Toyota","Land Cruiser")
car2 = Car("Hyundai","Verna")

print(car1.details())
print(car2.details())
    
# 2. When you want to enforce certain required parameters for an object
class User: 
    def __init__(self, username, email):
        if not username or not email:               # If some attributes are essential for the class to function correctly, a constructor ensures that those parameters are always provided when creating an object
            raise ValueError("Username and email are required")        
        self.username = username
        self.email = email

    def show_user(self):
        return f"User: {self.username}, Email: {self.email}"
    
user1 = User("geekyHimanshu","geekyHimanshu2309@gmail.com")
print(user1.show_user())

# 3. When setting up default values for Object Properties
# Sometimes, it is useful to set default values for attributes so that they have a meaningful state even if the user does not explicitly provide values
# Ensures every object gets reasonable default values.
# Allows flexibility to override defaults when needed.
class Employee:
    def __init__(self, name, role="SDE"):
        self.name = name
        self.role = role
    def show_details(self):
        return f"Employee Name: {self.name}, Employee role: {self.role}"
    
emp1 = Employee("Alice","Manager")
emp2 = Employee("Monish")   # No role provided, so default is used

print(emp1.show_details())
print(emp2.show_details())