def my_sum(*args):
    print(*args)
    return sum(args)

print(my_sum(1, 2, 3))  # RecursionError: maximum recursion depth exceeded in comparison
print(my_sum(1, 2, 3, 4, 5, 6))  # RecursionError: maximum recursion depth exceeded in comparison

# The sum function is calling itself recursively. This is an example of infinite recursion.