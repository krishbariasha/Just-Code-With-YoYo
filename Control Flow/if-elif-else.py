# now if but with else
#So the Syntax goes like
'''
if <condition>
    <block of code>
elif <condition>
    <block of code>    
else:
    <block of code>
'''

# now we will built a func where we will check 
#whether the value is positive or negative

user_input = input('Enter the value \n ~$ ')
user_input = int(user_input)

if user_input == 0:
    print('This number is Zero')
elif user_input> 0:
    print('The number is positive')    
else:
    print('This is a negative number')
    
    