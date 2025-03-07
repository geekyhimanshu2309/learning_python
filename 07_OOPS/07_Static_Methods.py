# Static methods : A static method in Python is  a method that belongs to a class rather than an instance. It does not require access to the instance(self) or the class (cls). Static methods are defined using the @staticmethod decorator.

# Key Characteristics of Static Methods
# ✅ No Access to Instance (self) – Cannot modify object-specific attributes.
# ✅ No Access to Class (cls) – Cannot modify class-level attributes.
# ✅ Used for Utility Functions – Ideal for operations that do not depend on class or instance data.

# When to Use Static Methods?
# 🔹 When a method does not need to access instance or class attributes.
# 🔹 When defining utility functions related to the class.
# 🔹 When performing operations independent of the class state.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Using static methods
print(TemperatureConverter.celsius_to_fahrenheit(25))  # Output: 77.0
print(TemperatureConverter.fahrenheit_to_celsius(77))  # Output: 25.0


# Real-World Example: Static Method in a Utility Class

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Using static methods
print(TemperatureConverter.celsius_to_fahrenheit(25))  # Output: 77.0
print(TemperatureConverter.fahrenheit_to_celsius(77))  # Output: 25.0
