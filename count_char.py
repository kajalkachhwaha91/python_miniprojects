


word = input("Enter a word: ")
x = (input("Enter a character to count: "))


res = 0
for i in word:
    if i == x:
        res += 1
    # break
print(res)
