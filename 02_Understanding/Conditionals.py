tea_varieties= ['Green tea', 'Black tea', 'White tea', 'Oolong tea', 'Herbal tea']
for tea in tea_varieties:
    print(tea)
    if tea == 'Oolong tea':
        print('I love Oolong tea!')
    else:
        print('I like ' + tea)

tea_varieties.pop()
print(tea_varieties)

tea_varieties.remove('White tea')
print(tea_varieties)

tea_varieties.insert(2, 'White tea')
print(tea_varieties)

tea_varieties_copy = tea_varieties          #This will not create a reference to the original list in memory
print(tea_varieties_copy)

tea_varieties_copy2 = tea_varieties.copy()   #This will create a reference to the original list in memory

tea_varieties_copy2.append('Lemon tea')         #This will not create a reference to the original list in memory

squared_numbers = [x*x for x in range(10)]
print(squared_numbers, "squared_numbers")

cubic_numbers = [x**3 for x in range(5)]
print(cubic_numbers, "cubic_numbers")

print("Range function: holds a list of numbers")
print("range(5) => [0, 1, 2, 3, 4]")
print("range(2, 5) => [2, 3, 4]")
print("range(0, 10, 2) => [0, 2, 4, 6, 8]")
print("range(10, 0, -2) => [10, 8, 6, 4, 2]")
print("range(5, 0, -1) => [5,4,3,2,1]")