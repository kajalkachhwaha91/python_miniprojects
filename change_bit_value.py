n = int(input())

# Convert to binary (remove '0b')
binary = bin(n)[2:]

# Toggle bits
toggled = ""
for bit in binary:
    if bit == '0':
        toggled += '1'
    else:
        toggled += '0'

# Convert back to decimal
result = int(toggled, 2)

print(result)