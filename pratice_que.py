numbers = [1, 2, 3, 4, 5]

# list comprehension
squares = [x**2 for x in numbers]

# dictionary comprehension
square_dict = {x: x**2 for x in numbers}

print(squares)
print(square_dict)