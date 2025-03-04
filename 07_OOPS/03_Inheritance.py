### Inheritance - It allows a class(child-class) to inherit properties and methods from another class(parent class), enabling code reusability and hierarchical relationships between classes.

# In python, a child class is created by passing the parent class as an argument inside parenthesis
# Example:

class Animal:
	def __init__(self,name):
		self.name = name
	def speak(self):
	    return "Sucess speaks itself"
  
class Dog(Animal):
  	def speak(self):
         return "Bark!!"
  
dog = Dog("Buddy")
print(dog.name)
print(dog.speak())

## Types of Inheritance in Python:

# a. Single inheritance: A single child inherits from single parent class

class Parent:
    def func1(self):
        print("This is the parent class")
    
class Child(Parent):
    def func2(self):
        print("This is the child class")
        
obj = Child()
obj.func1()
obj.func2()

# b. Multiple inheritance: A child class inherits from multiple parent class

class Parent1:
    def func1(self):
        print("This is parent1")
class Parent2:
    def func2(self):
        print("This is parent2")
        
class Child(Parent1, Parent2):
    def func3(self):
        print("This is child class")
        
mobj = Child()
mobj.func1()
mobj.func2()
mobj.func3()

# c. Multilevel inheritance: A class inherits from another class, which itself inherits from another class

class GrandParent:
    def func1(self):
        print("This is grand parent class")
class Parent(GrandParent):
    def func2(self):
        print("This is parent class")
class Child(Parent):
    def func3(self):
        print("This is child class")
        
Mobj = Child()
Mobj.func3()
Mobj.func1()
Mobj.func2()

# d. Hierarchical inheritance: Multiple child class inherit from the same parent class

class Parent:
    def func1(self):
        print("This is Parent class")
        
class Child1(Parent):
    def func2(self):
        print("This is child1 inheriting from parent")

class Child2(Parent):
    def func3(self):
        print("This is child2 inheriting from parent")

obj1 = Child1()
obj2 = Child2()

obj1.func1()
obj1.func2()

obj2.func1()
obj2.func3()

# e. Hybrid inheritance: combination of multiple inheritance types

class A:
    def func1(self):
        print("This is A")
class B(A):
    def func2(self):
        print("This is B inheriting from A")
        
class C(A):
    def func3(self):
        print("This is C inheriting from B")

class D(B,C):
    def func4(self):
        print("This is class D")
        
objD = D()
objD.func1()
objD.func2()
objD.func3()
objD.func4()


# super() Keyword
# super() function allows a child class to call methods and constructor of the parent class

class AnimalCow:
    def __init__(self,name):
        self.name= name
class Cow(AnimalCow):
    def __init__(self, name,breed):
        super().__init__(name)					# calling parent constructor -> self.name = name
        self.breed = breed
        
cow = Cow("Cute","Gharelu")
print(cow.breed)
print(cow.name)

#NOTE: Method_Resolution_Order_(MRO)
# MRO determines the sequence in which methods are inherited from parent classes. Python uses the C3 linearization (or MRO algorithm)


## Diamond Problem: The diamond problem occurs in multiple inheritance when a class inherits from two parent classes that both inherit from the same grandparent class. This creates an ambiguity in method resolution.
# Example of Diamond problem:
class A:
    def show(self):
        print("A")
        
class B(A):
    def show(self):
        print("B")
        
class C(A):
    def show(self):
        print("C")
class D(B,C):
    def show(self):
        print("D")
        
objDiamond = D()
objDiamond.show()
# Both B and C have a show() method. If D calls show(), which class should Python prioritize—B or C?

# How python solves the diamond problem?

# Python uses Method Resolution Order (MRO) to determine the order in which classes are searched for a method.
# It follows the C3 linearization algorithm, which ensures that:
# 1. Children come before parents
# 2. Preserves the order in which classes were inherited
# 3. Ensures no duplicate method resolution

print(D.mro())