print("Hello! Welcome to grade converter!")
# student_score = input("What is your score? (0-100)")
student_score = int(input("What is your score? (0-100)....."))
if 97 <= student_score <= 100:
   grade = "A+"
elif student_score in range(92,95):
   grade = "A"
elif student_score in range(89,91):
   grade = "A-"   
elif student_score in range(86,88):
   grade = "B+"
elif student_score in range(82,85):
   grade = "B"
elif student_score in range(79,81):
   grade = "B-"
elif student_score in range(76,78):
   grade = "C+"
elif student_score in range(72,75):
   grade = "C"
elif student_score in range(69,71):
   grade = "C-"
elif student_score in range(66,68):
   grade = "D+"
elif student_score in range(62,65):
   grade = "D"
elif student_score in range(59,61):
   grade = "D-"
elif student_score in range(56,58):
   grade = "F+"
elif student_score in range(52,55):
   grade = "F"
elif student_score in range(0,51):
   grade = "F-"
else:
   print("Please enter valid score. (0-100)")
# print result
if student_score > 71:
  print(f"Your {student_score} yields a letter grade of {grade}. Great job and keep up the great work")
else:
  print(f"Your {student_score} yields a letter grade of {grade}. Work harder next time and please improve your results!!")