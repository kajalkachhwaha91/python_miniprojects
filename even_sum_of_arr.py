n = int(input())
ele = list(map(int, input().split()))

# Ensure only n elements are taken
ele = ele[:n]

freq = {}

for i in ele:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

found = False

for i in freq:
    if freq[i] % 2 == 0:
        print(i, end=" ")
        found = True

if not found:
    print(-1)