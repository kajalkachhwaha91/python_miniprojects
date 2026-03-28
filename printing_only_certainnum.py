n = int(input())
ele = list(map(int, input().split()))
ele = ele[:n]


# for x in ele:
#     if x not in [0,1,2,3]:
#         print("Invalid input")
#         exit()

# sorting
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if ele[j] > ele[j+1]:
            ele[j], ele[j+1] = ele[j+1], ele[j]
            swapped = True
    if not swapped:
        break

print(ele)