def display_grade(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks")
    elif marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

marks = float(input("Enter marks: "))
display_grade(marks)
