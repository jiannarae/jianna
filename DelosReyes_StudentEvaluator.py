# Delos Reyes, Jianna
# 8 - Camia

#Global Variables
name = input("Enter Student Name: ")
score1, score2, score3 = (0,0,0)
average = (score1 + score2 + score3)/3
performance = ""

# TITLE
def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")
    print("-"*10)


# GETTING STUDENTS ASSESSMENT SCORES
def get_student_info():
    input(name)
    score1 = float(input("Enter Assessment 1: "))
    score2 = float(input("Enter Assessment 2: "))
    score3 = float(input("Enter Assessment 3: "))
    return score1, score2, score3


def evaluate_student_info():
    input(average)
    if 90<=average<=100:
        performance = "Outstanding"
    elif 85<=average<90:
        performance = "Very Satisfactory"
    elif 80<=average<85:
        performance = "Satisfactory"
    elif 75<=average<80:
        performance = "Fairly Satisfactory"
    else:
        print("Needs Improvement")
    return performance, average


def display_result():
    print("STUDENT PERFORMANCE REPORT")
    print(name)
    print(f"Assessment Scores: {score1, score2, score3}")
    print(f"Average Score: {average:.2f}")
    print(f"Performance Level: {performance}")

display_header()
get_student_info()
evaluate_student_info()
display_result()
