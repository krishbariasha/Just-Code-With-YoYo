marks = int(input("Enter Your Marks : "))

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >=60:
    grade = 'D'
elif marks >= 50:
    grade = 'E'
else:
    grade = 'Fail'


print('The grade obtained is: ', grade)



