#Grading system
score = int(input("Enter the student's score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 80:
    print("A")
elif score >= 60:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")