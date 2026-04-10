print("Title: Student Result and Eligibility System")

# Input Requirements:

name = input("Enter your Name: ")

# Truthy/Falsy Check:
if not name:
    print("Invalid Name Input")
else:
    print("Wwlcome!", name)

math = int(input("Enter your marks (Math): "))
english = int(input("Enter your marks (English): "))
science = int(input("Enter your marks (Science): "))
attendance = int(input("Enter your attendance: "))

# Pass/Fail Condition:

if math and english and science < 33:
    print("You Failed")
    print("Better luck next time.")
else: 
    print("Congratulations!!! You Passed.")

# Grade Calculation:

avg = (math + english + science)/3

if avg >= 80:
    print("Grade: A")
elif avg >= 70:
    print("Grade: B")
elif avg >= 60:
    print("Grade: C")
elif avg >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# Scholarship Eligibility:

if avg >= 33:
    if avg >= 75:
        if attendance >= 80:
            print("You are eligible for Scholarship!!")
        else:
            print("No Scholarship. Your attendance is not enough.")
    else:
        print("No Scholarship! Your average number is below 75.")
else:
    print("Sorry! Your number is not enough for scholarship! ")

# Warning System (Nested Condition):

if math < 40:
    print("Warning: Try to improve in", ["MATH"])
elif english < 40:
    print("Warning: Try to improve in", ["ENGLISH"])
elif science < 40:
    print("Warning: Try to improve in", ["SCIENCE"])
else: 
    if math and english and science >= 90:
        print("Excellent Performance!")
    else:
        print("Good job!! Keep improving.")


