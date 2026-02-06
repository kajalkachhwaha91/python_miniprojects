stuName = str(input("Enter your name:"))
stuAge = int(input("Enter your age:"))
stuMarks = float(input("Enter your marks:"))
catagery = input("Enter your catagery:").upper()

if stuMarks >= 90:
    print(stuName, "You are eligible  for scholarship. you hve to pay only 20,000")
elif stuMarks >= 85:
    print(stuName, "You are eligible  for scholarship. you hve to pay only 30,000")
elif stuMarks >= 75 and catagery in ["OBC", "SC", "ST"]:
    print(stuName, "You are eligible  for scholarship. you hve to pay only 30,000")
else:
    print(stuName, "You are not eligible  for scholarship")


if stuAge >= 18:
    print(stuName, "You are an adult")
else:
    print(stuName, "You are minor")

if stuMarks >= 90:
    print(stuName, "excellenet performance")  
elif stuMarks >= 75:
    print(stuName, "good performance")
else:
    print(stuName, "Needs Improvement")