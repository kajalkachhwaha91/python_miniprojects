
str_input = str(input().lower())
freq = {}
p = int(input("Enter the number of occurrence you want to find: "))
	
for ch in str_input:
  if ch in freq:
    freq[ch] += 1
  else:
    freq[ch] = 1
		
for i in freq:
   print(freq[i], i)

res = []
		
for i in freq:
  if freq[i] >= p:
	  res.append(i)
  

if res:
  print("The characters that occur more than or equal to", p, "times are:", res)
else:  print("No characters occur more than or equal to", p, "times.")
