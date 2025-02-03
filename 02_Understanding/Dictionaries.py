print("Dictionaries")

# Dictionaries are a collection of key-value pairs. They are unordered, changeable, and indexed. In Python, dictionaries are defined using curly braces {}. Each key-value pair in a dictionary is separated by a colon :. The key and value can be of any data type. The key must be unique within a dictionary, but the values can be duplicated.

chai_types={"Masala": "Spicy", "Ginger": "Strong", "Green": "Herbal", "Black": "Strong", "Lemon": "Citrus"}
print(chai_types["Masala"])       #Output: Spicy

# You can also use the get() method to access the value of a key in a dictionary. The get() method returns None if the key is not found in the dictionary, while direct access using square brackets [] raises a KeyError.

print(chai_types.get("Ginger"))       #Output: Strong
print(chai_types.get("Oolong"))       #Output: None

print("If, I will try to get a value of a key that doesn't exist in the dictionary, it will return None. But, if I try to get a value of a key that doesn't exist in the dictionary using square brackets, it will raise a KeyError.")

# You can add new key-value pairs to a dictionary by assigning a value to a new key. If the key already exists in the dictionary, the value associated with that key is updated.

chai_types["Oolong"] = "Light"
print(chai_types)       #Output: {'Masala': 'Spicy', 'Ginger': 'Strong', 'Green': 'Herbal', 'Black': 'Strong', 'Lemon': 'Citrus', 'Oolong': 'Light'}
chai_types["Masala"] = "Spicy and Aromatic"      #Updating the value of an existing key

# You can remove a key-value pair from a dictionary using the del keyword followed by the key you want to remove.

del chai_types["Lemon"]
print(chai_types)       #Output: {'Masala': 'Spicy and Aromatic', 'Ginger': 'Strong', 'Green': 'Herbal', 'Black': 'Strong', 'Oolong': 'Light'}

# You can also use the pop() method to remove a key-value pair from a dictionary. The pop() method takes the key as an argument and returns the value associated with that key. If the key is not found in the dictionary, the pop() method raises a KeyError.

chai_types.pop("Green")
print(chai_types)       #Output: {'Masala': 'Spicy and Aromatic', 'Ginger': 'Strong', 'Black': 'Strong', 'Oolong': 'Light'}

# You can use the keys() method to get a list of all the keys in a dictionary. Similarly, the values() method returns a list of all the values in a dictionary.

print(chai_types.keys())        #Output: dict_keys(['Masala', 'Ginger', 'Black', 'Oolong'])
print(chai_types.values())      #Output: dict_values(['Spicy and Aromatic', 'Strong', 'Strong', 'Light'])

def loopsInDictionary():
  print("Print all keys in the dictionary using square brackets")
  for key in chai_types:
    print(key, chai_types[key])
  print("Key, Value")
  for key, value in chai_types.items():           # we will use items() method to get both key and value
    print(key, value)           
  
loopsInDictionary()

print(len(chai_types), "Length of chai types dictionary")       #Output: 4

chai_types.popitem()       #Removes the last key-value pair from the dictionary. No need for any parameter

chai_types_copy = chai_types.copy()       #Create a copy of the dictionary
print(chai_types_copy)       #Output: {'Masala': 'Spicy and Aromatic', 'Ginger': 'Strong', 'Black': 'Strong'}

chai_types.clear()      #Clear all key-value pairs from the dictionary
print(chai_types)       #Output: {}

# Nested Dictionaries
# You can create dictionaries where the values are also dictionaries. This is known as a nested dictionary. Nested dictionaries are useful for representing hierarchical data structures.

chai_types = {
    "Masala": {
        "Flavor": "Spicy",
        "Caffeine": "Low"
    },
    "Ginger": {
        "Flavor": "Strong",
        "Caffeine": "High"
    },
    "Green": {
        "Flavor": "Herbal",
        "Caffeine": "Low"
    }
}      #Nested dictionary

print(chai_types["Masala"]["Flavor"])       #Output: Spicy
print(chai_types["Ginger"]["Caffeine"])       #Output: High

# Dictionary Comprehension
# Dictionary comprehension is a concise way to create dictionaries in Python. It is similar to list comprehension, but it creates dictionaries instead of lists. Dictionary comprehension uses curly braces {} to create dictionaries.

squared_num = {x: x*x for x in range(5)}
print(squared_num)       #Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

