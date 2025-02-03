def whatIsList(): 
  print("In Python, a list is a mutable, ordered collection of items. Lists can contain elements of different types, including other lists. They are one of the most commonly used data structures in Python due to their flexibility and ease of use.")
  print("Key characteristics of lists in Python:")
  print("Ordered: Lists maintain the order of elements in which they are added.")
  print("Mutable: Lists can be modified after they are created.")
  print("Dynamic: Lists in Python can grow and shrink in size as needed.")
  print("Heterogeneous: Lists can contain elements of different types.")

tea_varieties = ['Green tea', 'Black tea', 'White tea', 'Oolong tea', 'Herbal tea']
my_list = [1, "hello", 3.14, [2, 4, 6]]
tea_varieties[3] = "Herbal tea"

print(tea_varieties)
tea_varieties[1:2]
tea_varieties[1:2] = "Lemon"      #Every element of Lemon will be treated as single array elements
print(tea_varieties)

tea_varieties= ['Green tea', 'Black tea', 'White tea', 'Oolong tea', 'Herbal tea']
tea_varieties[1:2] = ["Lemon"]
print(tea_varieties)