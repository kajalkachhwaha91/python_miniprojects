password = input("Enter your password: ")

if len(password) >= 8 and any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in "@#$%" for char in password):   
    print("Password is strong. you can signup")
else:
    print("Password is weak,try with strong password")