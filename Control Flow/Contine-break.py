# break and continue statement in python both of these are use within loop

'''
syntx is very simple just right 
break
or 
continue
within the loop
'''

# while True:
#     break
#     print("infinite")
#     break
# print('out of the loop')

# while True:
#     print("infinite")
#     break
# print('out of the loop')

# counter = 0
# while counter <= 100:
#     counter += 1
#     if counter == 100:
#         print(counter)
#     continue

# print('out of the loop')



attempt = 0
MAX_ATTEMPTS = 4
correct_pin = "1234"

while attempt < MAX_ATTEMPTS:
    user_pin = input('enter your pin: \n ~$ ')
    
    if not user_pin:
        print('You did not enter the pin, please enter the pin')
        continue
    if user_pin == correct_pin:
        print('Please wait while we process your request')
        break
    else:
        attempt += 1
        print(f"Incorrect pin {MAX_ATTEMPTS - attempt} attempts remaining")
        
if attempt == MAX_ATTEMPTS:
    print("Too many attempts , Card Blocked")
    
print('Thanks for Using demo ATM')