# Encapsulation: Encapsulation is one of the fundamental principles of OOP. It is the mechanism of restricting direct access to certain details of an object and only exposing the necessary functionalities.

class Animal:
  def __init__(self,name):
    self.name = name
  def get_name(self):
    return f"This is {self.name} !!"
  def speak(self):
	    return "Sucess speaks itself"
  
class Dog(Animal):
  	def speak(self):
         return "Bark!!"
  
dog = Dog("Buddy")
print(dog.name)
print(dog.speak())

# How encapsulation works in Python?
# Python uses private, protected, and public access specifiers to enforce encapsulation

# Access modifiers: 
# Public (No prefix) : Accessible from anywhere
# Protected (_ single underscore): Meant for internal use, but still accessible
# Private (__ double underscore): Not accessible directly outside the class

# Classes with encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public variable
        self._balance = balance  # Protected variable
        self.__pin = "1234"  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self._balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

    def __get_pin(self):  # Private method
        return self.__pin

# Creating an object
account = BankAccount("123456789", 1000)

# Accessing public variable
print(account.account_number)  # Allowed

# Accessing protected variable (allowed, but not recommended)
print(account._balance)  # Works, but should be avoided

# Trying to access a private variable (will cause an error)
# print(account.__pin)  # AttributeError

# Accessing private variable using name mangling
print(account._BankAccount__pin)  # Works, but not recommended


# Benefits of encapsulation:
# 1. Data hiding - Prevents accidental modifications to sensitive data
# 2. Code maintainability - Helps keep the code organized and modular
# 3. Increased Security - Prevents direct modification of critical attributes
# 4. Encapsulated Logic - Controls how data is accessed and modified through methods.

