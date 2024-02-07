#the multiple elif conditions\\
    #like grade of a student
    
marks = int(input('Enter The Obtain Marks \n ~$ '))

if marks >= 90:
     grade = 'A'
elif marks >= 80:
     grade = 'B'
elif marks >=70:
     grade = 'C'
elif marks >= 60:
     grade = 'D'
else:
    grade = 'E'         

print('The grade obtained is: ', grade)    