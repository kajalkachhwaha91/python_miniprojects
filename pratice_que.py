# # q.1
# numbers = [1, 2, 3, 4, 5]

# # list comprehension
# squares = [x**2 for x in numbers]

# # dictionary comprehension
# square_dict = {x: x**2 for x in numbers}

# print(squares)
# print(square_dict)


# # q.25
# def check_even(func):
#     def wrapper(*args, **kyargs):
#         print("processing numbers")
#         func(*args, **kyargs)
#         print("processing complete")

#     return wrapper


# lst = [1, 2, 3, 4, 5, 6]


# @check_even
# def print_even_num(lst):
#     even_num = [num for num in lst if num % 2 == 0]
#     print("Even list:", even_num)
#     squ_dict = {num: num**2 for num in even_num}
#     print("Square dictionary:", squ_dict)


# print_even_num(lst)


# q.3



n = int(input())

arr = list(int(input().split()))

for i in range(n):
    count = 0
    for i in arr:
        count += 1
print(count)

