import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return [area, circumference]  # Return a list or can return a tuple your choice

print(circle_stats(5))

