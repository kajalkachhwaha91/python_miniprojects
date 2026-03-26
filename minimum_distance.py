

arr = list(map(int, input().split()))
x = int(input())
y = int(input())

last_pos = -1
min_dist = float('inf')

for i in range(len(arr)):
  if arr[i] == x or arr[i] == y:
    
    if last_pos != -1 and arr[i] != arr[last_pos]:
      min_dist = min(min_dist, i - last_pos)
	  
    last_pos = i
	
if min_dist == float('inf'):
  print("-1")
else:
  print(min_dist)