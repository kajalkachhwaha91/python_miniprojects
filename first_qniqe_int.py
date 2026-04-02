s = list(map(int, input().split()))
freq = {}

# Count frequency
for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# Find first unique
for i in s:
    if freq[i] == 1:
        print(i)
        break
else:
    print(-1)