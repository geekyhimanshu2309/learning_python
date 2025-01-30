#himan@GeekyHimanshu MINGW64 ~/Documents/Python learning (01_basic)
#$ python
#Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> username = "geekyHimanshu"
#>>> username
#'geekyHimanshu'
#>>> username = "chaiaurCode"
#>>> username
#'chaiaurCode'
#>>> 
def mutable():
  print("Mutable and Immutable Objects in Python")
  print("Mutable objects")
  print("Mutable objects are those whose state can be changed after they are created. Examples of mutable objects in Python include:")
  print("Lists")
  print("Dictionaries")
  print("Sets")
  print("User-defined classes")
  print("Creating a list (mutable object)")
  print("my_list = [1, 2, 3]")
  print("my_list") 
  print("Modifying an element of the list")
  print("my_list[0] = 10")
  print("my_list")
  print("Immutable objects")
  print("Immutable objects are those whose state cannot be changed after they are created. Examples of immutable objects in Python include:")
  print("Numbers")
  print("Strings")
  print("Tuples")
  print("Float")
  print("Creating a string (immutable object)")
  print("# Initial assignment")
  print("username = 'geekyHimanshu'")
  print("username - # Output: 'geekyHimanshu'")  
  print("# Reassignment to a new string")
  print("username = 'chaiaurCode'")
  print("username - # Output: 'chaiaurCode'")  

mutable()
def key_differences():
  print("Immutable objects: Cannot be changed after creation. Any modification results in a new object.")
  print("Mutable objects: Can be changed after creation. Modifications affect the original object.")

key_differences()