# total_marks greater then equal to 80 then Grade A+
# total marks greater then equal to 60 and less then 80 then Grade B
# total marks greater then equal to 40 and less then 59 then Grade C
# otherwise Grade F

total_marks = 42

if total_marks >= 80:
    print("A+")

elif total_marks >= 60 and total_marks < 80:
    print("B")
elif total_marks >= 40 and total_marks < 60:
    print("C")
else:
    print("F")