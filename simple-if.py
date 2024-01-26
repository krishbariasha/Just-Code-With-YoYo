##




## Syntax
# the condition has to evaluate to a boolean block \
#code can contain any python code
'''
    if <condition>:
        <block of code>

'''

## Example 1

#
# check wether the number given by the user
# as unput is even or odd


user_input = input('Enter a number: \n ~$ ')
user_input = int(user_input)


if user_input % 2 == 0:
    print("The number is Even")

if user_input %2 != 0:
    print('The number is Odd')