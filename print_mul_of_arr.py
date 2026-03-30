import math
n = int(input())
# p =1
# for i in n:
#     p *= int(i)
# print(p)


if n % 100 == 0:
    print(n// 100)
else:
    print(n// 100 + 1)



n = int(input())
print(math.ceil(n / 100))