# number guessing game


import random


random_number = random.randint(1, 30)
MAX_ATTEMPT = 4
current_attempt = 0

while current_attempt < MAX_ATTEMPT:
    user_guess = int(input("Guess the number: "))
    if user_guess == random_number:
        print('You Won !')
        break
    else:
        current_attempt += 1
else:
    print('YOU HAVE EXHAUSTED ALL THE ATTEMPTS \n TRY AGAIN')
    
print('The Random Number was: ', random_number )
