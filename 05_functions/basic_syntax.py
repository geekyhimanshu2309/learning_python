def square(num):
  return num*num

# squared_num = {x: square(x) for x in range(5)}

num = int(input("Enter a number: "))

print("Square of", num, "is", square(num))