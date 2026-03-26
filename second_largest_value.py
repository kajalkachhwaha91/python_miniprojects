# with improvemnet so that it can handle the negative, float value with proper resuklts.

arr = [ -2, 0.4, 0, -7, 8,0, 4, 0,5, 2]
lar = float('-inf')
sec = float('-inf')

for num in arr:
    if num > lar:
        sec = lar
        lar = num
    elif num > sec and num != lar:
        sec = num    

print("Second largest number is:", sec)
0




    
    






