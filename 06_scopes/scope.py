username = "chai aur himanshu"

def func():
    username = "chai"
    print(username)

func()
print(username,"username")

x = 99
def func2(y):
    z = x+y
    return z

result = func2(10)

print(result)


def func3():
    x = 88
    def func4():
        print(x)
    func4()

func3()

# Closures: Bag theory

def func5():
    x = 88
    def func6():
        print(x)
    return func6
myresult = func5()
myresult()
# On returning the reference of a function not only the function is returned, reference value of variables associated with that function is also returned is known as 

# Factory functions

def chaiCoder(num):
    def actual(x):
        return x**num
    print(actual)
    return actual

f = chaiCoder(2)
print(f)
print(f(5))