print("Hello! Welcome to grade converter!")
# student_score = input("What is your score? (0-100)")
student_score = int(input("What is your score? (0-100)....."))
if 90 <= student_score <= 100:
   grade = "A"
elif student_score in range(80,90):
   grade = "B"
elif student_score in range(70,79):
   grade = "C"
elif student_score in range(60, 69):
   grade = "D"
elif student_score in range(0,59):
   grade = "F"
else:
   print("Please enter valid score. (0-100)")
# print result
print(f"Your {student_score} yields a letter grade of {grade}.")