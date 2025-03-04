class Animal:
  def __init__(self,name):
    self.name = name
  def get_name(self):
    return f"This is {self.name} !!"
  def speak(self):
	    return "Sucess speaks itself"
  
class Dog(Animal):
  	def speak(self):
         return "Bark!!"
  
dog = Dog("Buddy")
print(dog.name)
print(dog.speak())