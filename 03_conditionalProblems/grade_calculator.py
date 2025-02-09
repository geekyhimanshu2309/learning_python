print("Enter marks scored : ")
marks = int(input())

if(marks > 100):
    print("Invalid marks")
    exit()

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F" 

print("Grade: ", grade) 

