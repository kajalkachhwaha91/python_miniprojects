# Create a class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("hello , my name is", self.name)


# Create an object
p1 = Person("Kajal", 36)

# Call the greet method
p1.greet()


# Create another class for init method
#  Create the Dog class
class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print(self.name + " says Woof!")

# Create an object
d1 = Dog("Buddy", 3)

# Call the bark method
d1.bark()
