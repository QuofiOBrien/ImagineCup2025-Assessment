 #STUDENTS RESULTS COMPUTATION SYSTEM

import re
# =============== HEADER ===============
print ("\n☺ SCHOLARO ASSESSMENT SYSTEM ☺")
print ("\n" + "=" * 30)

# =============== STUDENT PROFILE ===============
print ("\n" + "=" * 30)
print ("STUDENT PROFILE")
while True:
    student_name = input("Enter your full name: ").strip().upper()
    if not student_name:
        print ("Invalid input!!! Name cannot be empty.")
        continue

    if re.fullmatch (r"[A-Za-z]+([ '-][A-Za-z]+)*", student_name):
        print (f"Student name = {student_name}.")
        break
    else:
        print ("Invalid input!!! Support names containing  letters, spaces and hyphens ")

while True:
    student_id = input("Enter your Student ID (e.g., PU/CS/2025/007): ").strip().upper()
    pattern = r'^[A-Z]{2,3}/[A-Z]{2,3}/\d{4}/\d{1,4}$'
    if re.match (pattern, student_id):
        last_part = student_id.split ('/')[-1]
        if int (last_part) >= 0:
            print (f"Student ID Number = {student_id}.")
            break
        else:
            print("Invalid! Last part of ID cannot be negative.")
    else:
        print("Invalid format! Use: XX/XX/2025/000 ")


# =============== COURSE NAMES ===============
print ("\n" + "=" * 30)
print ("COURSE NAMES")
course_1 = input ("Enter the Course 1: ").strip().upper()
print (f"Course 1 = {course_1}.")
course_2 = input ("Enter the Course 2: ").strip().upper()
print (f"Course 2 = {course_2}.")
course_3 = input ("Enter the Course 3: ").strip().upper()
print (f"Course 3 = {course_3}.")


# =============== SCORES ASSESSMENT ===============
print ("\n" + "=" * 30)
print ("SCORES ASSESSMENT")

def valid_score (course_name):
    while True:
        try:
            score = float (input (f"Enter score for {course_name} (0–100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input!!! Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input!!! Please enter a valid number.")

scores_for_course_1 = valid_score (course_1)
print (f"Score for {course_1} = {scores_for_course_1}")
scores_for_course_2 = valid_score (course_2)
print (f"Score for {course_2} = {scores_for_course_2}")
scores_for_course_3 = valid_score (course_3)
print (f"Score for {course_3} = {scores_for_course_3}")

scores = [scores_for_course_1, scores_for_course_2, scores_for_course_3]


# =============== SUM & AVERAGE ===============
print ("\n" + "=" * 30)
print ("SUM OF SCORES")
total = sum(scores)
print (f"Sum of scores = {total:.2f}")

print ("\n" + "=" * 30)
print ("AVERAGE OF SCORES ACCUMULATED")
average = (total) / 3
print (f"Average of scores = {average:.3f}")


# =============== GRADE CALCULATOR ===============
print("\n" + "=" * 30)
print("GRADE CALCULATOR")

def grade (scores):
    if scores >= 80:
        return "A"
    elif scores >= 70:
        return "B"
    elif scores >= 60:
        return "C"
    elif scores >= 50:
        return "D"
    else:
        return "F"


# =============== INDIVIDUAL COURSE GRADES ===============
print(f"{student_name}'s grade for {course_1} = {grade(scores_for_course_1)}")
print(f"{student_name}'s grade for {course_2} = {grade(scores_for_course_2)}")
print(f"{student_name}'s grade for {course_3} = {grade(scores_for_course_3)}")


# =============== GPA CALCULATOR ===============
print ("\n" + "=" * 30)
print ("GPA CALCULATOR")

def grade_point (grade):
    if grade == "A":
        return 3.0
    elif grade == "B":
        return 2.5
    elif grade == "C":
        return 2.0
    elif grade == "D":
        return 1.5
    else:
        return 0.0

grade_1 = grade (scores_for_course_1)
grade_2 = grade(scores_for_course_2)
grade_3 = grade(scores_for_course_3)


gpa =   (grade_point (grade_1) + grade_point (grade_2) + grade_point (grade_3)) / 3
print (f"GPA = {gpa:.2f}")


# =============== OVERALL REMARK BASED ON GPA ===============
if gpa >= 2.75:
     remark = "Excellent! You're a top performer! 🌟"
elif gpa >= 2.25:
    remark = "Good work. Keep pushing! 💪"
elif gpa >= 1.75:
    remark = "Good. Room for improvement. 📈"
elif gpa >= 1.0:
    remark = "Pass. Study harder next semester. 📚"
else:
    remark = "Failed. Retake required. 🔄"
print (f"Remark : {remark}")

# =============== FOOTER ===============
print("\n" + "=" * 30)
print("System closed. Thank you! 🇬🇭")
print("Imagine Cup 2025 – Ghana Representing! 🚀")
print ("https://github.com/QuofiOBrien")
