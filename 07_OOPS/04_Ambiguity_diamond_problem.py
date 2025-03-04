# class A:
#     def show(self):
#         print("Class A")

# class B(A):
#     def show(self):
#         print("Class B")

# class C(A):
#     def show(self):
#         print("Class C")

# class D(B, C):  # Multiple inheritance
#     pass

# obj = D()
# obj.show()


class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()  # Calls next class in MRO
        print("Class B")

class C(A):
    def show(self):
        super().show()
        print("Class C")

class D(B, C):
    def show(self):
        super().show()
        print("Class D")

obj = D()
obj.show()

# Conclusion
# Python avoids the diamond problem using the MRO (C3 Linearization Algorithm).
# super() ensures proper method execution across multiple levels.
# MRO ensures a clear hierarchy, preventing ambiguity in method resolution

# What is Ambiguity? 🤔
# Ambiguity refers to uncertainty or confusion that arises when something can be interpreted in multiple ways, and there is no clear resolution.

# Ambiguity in Programming 
# In programming, ambiguity occurs when the compiler or interpreter cannot determine which method, variable, or operation to execute due to conflicting definitions.

# Example: Ambiguity in Multiple Inheritance (Diamond Problem)
# When a class inherits from two parent classes that both have the same method, the derived class does not know which method to call.