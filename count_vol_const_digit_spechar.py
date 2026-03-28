
s = input()
vol_count =0
cons_count = 0
digit =0
special_char =0

for ch in s:
 if ch in "aeiou" :
   vol_count+=1
 elif ch.isalpha():
   cons_count+=1
 elif ch.isdigit():
   digit+=1
 else:
   special_char+=1
    
    

print(vol_count, cons_count , digit , special_char , end ="")

