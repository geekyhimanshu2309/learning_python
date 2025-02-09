# Age group categorization

# Write a program that reads a person's age and prints the age group they belong to. The age groups are as follows:

age = int(input("Enter your age: "))

if age < 13:                              # Parentheses are not required in Python, it's optional                
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
