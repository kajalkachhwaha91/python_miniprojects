# older form of list
cube = []
for x in range(10):
    cube.append(x**3)
print(cube)

# optimized code using list comprehension
# [expression for item in iterable if condition]
cube = [x**3 for x in range(10)]
print(cube)


# older form of dictionary
cube = {}

for x in range(5):
    cube[x] = x**3
print(cube)

# optimized code using dictionary comprehension
cube = { x : x**3 for x in range(5) }
print(cube)

