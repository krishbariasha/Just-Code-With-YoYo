


## Domain: Ecomm.

## Calulate discount


# electronics / clothing / other

## "INDIA" , 'USA'


prompt_category = '''
Please choose the Item: \n
1. Electronics | Press-1 \n
2. Play-Station | Press-2 \n
3. Clothing | Press-3 \n
4. Other | Press-4 \n
>>>
'''

product = int(input(prompt_category))

prompt_location = '''
Please choose the location: \n
1. India | Press-1 \n
2. USA | Press-2 \n
3. Pakistan | Press-3 \n
'''

location = int(input(prompt_location))

if product == 1:
    if location == 1:
        discount = 20
    elif location ==3:
        discount=50
    else:
        discount = 5
elif product == 2:
    if location ==1:
        discount = 5
    elif location ==3:
        discount=50
    else:
        discount= 1
elif product == 3:
    if location == 1:
        discount= 10
    elif location ==3:
        discount=50
    else:
        discount= 2
elif product ==4:
    if location==3:
        print("Sorry NO Discount Available at that moment")
else:
    discount= 3

print('Applicable Discount is: ', discount)           
    