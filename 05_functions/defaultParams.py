def greet(name = "User"):
    print(f"Hello, {name}!")                      # f is known as formatted string literal
    
greet('Alice')  # Hello, Alice!
greet()        # Hello, User!              # Default parameter is used