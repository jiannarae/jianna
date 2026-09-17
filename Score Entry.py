# STUDENT SCORE ENTRY

try:
    exam_score = int(input("Enter your examination score: "))
    if 0 <= exam_score <= 100:
        print("Valid Score")

except ValueError:
     print("Invalid input. Please enter a number")