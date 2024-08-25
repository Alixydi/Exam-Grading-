#Class Grading 
score = int(input("What is your exam score?: "))
grade = None

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Feedback
if grade == 'A':
    print("Excellent! You've earned an A.")
elif grade == 'B':
    print("Well done! You've earned a B.")
elif grade == 'C':
    print("Good job! You've earned a C.")
elif grade == 'D':
    print("You've earned a D. Keep pushing!")
else:
    print("Unfortunately, you've earned an F. Don't lose heart, try again.")
