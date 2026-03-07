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
