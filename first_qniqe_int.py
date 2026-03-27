

s = list(map(int, input().split()))
freq = {}

for i in s:
  if s[i] in freq:
    freq[i] += 1
  else:
    freq[i] = 1
	
for i in s:
  if freq[i] == 1:
    print(i)
    break
else:
  print(-1)