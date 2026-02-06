stuName = str(input("Enter your name:"))
stuAge = int(input("Enter your age:"))
stuMarks = float(input("Enter your marks:"))
catagery = input(str("Enter your catagery:"))

if stuMarks >= 85 :
    print(stuName, "Eligible for scollarship")
else:
    print(stuName, " Sorry you are Not Eligible for scollarship")

if stuMarks >= 75 and catagery == "reserved":
    print(stuName, "Eligible for scollarship")