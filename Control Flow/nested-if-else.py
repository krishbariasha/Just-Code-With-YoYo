


# ## Domain: Ecomm.

# ## Calulate discount


# # electronics / clothing / other

# ## "INDIA" , 'USA'


# prompt_category = '''
# Please choose the Item: \n
# 1. Electronics | Press-1 \n
# 2. Play-Station | Press-2 \n
# 3. Clothing | Press-3 \n
# 4. Other | Press-4 \n
# >>>
# '''

# product = int(input(prompt_category))

# prompt_location = '''
# Please choose the location: \n
# 1. India | Press-1 \n
# 2. USA | Press-2 \n
# 3. Pakistan | Press-3 \n
# '''

# location = int(input(prompt_location))

# if product == 1:
#     if location == 1:
#         discount = 20
#     elif location ==3:
#         discount=50
#     else:
#         discount = 5
# elif product == 2:
#     if location ==1:
#         discount = 5
#     elif location ==3:
#         discount=50
#     else:
#         discount= 1
# elif product == 3:
#     if location == 1:
#         discount= 10
#     elif location ==3:
#         discount=50
#     else:
#         discount= 2
# elif product ==4:
#     if location==3:
#         print("Sorry NO Discount Available at that moment")
# else:
#     discount= 3

# print('Applicable Discount is: ', discount)           
    
    
prompt_category = '''
Please Choose an Item From The Given List: \n
1. Electronics | Press 1 \n
2. Clothing | Press 2 \n
3. Accessories | Press 3 \n
4. Mobile Phones | Press 4 \n
5. Grocessories | Press 5 \n
6. Other | Press \n
>>>
 '''   
product = int(input(prompt_category))

prompt_location = '''
Please Choose The Location : \n
1. India | Press 1 \n
2. Pakistan | Press 2 \n
3. USA | Press 4 \n
4. Afghanistan | Press 5 \n
5. Europe | Press 6 \n
6. Other Country
>>>       
'''

location = int(input(prompt_location))

if product == 1:
    if location == 1:
        # India location
        discount = 20
    elif location == 2:
        #Pakistan
        discount = 15
    elif location == 3:
        #USA
        discount = 7
    elif location == 4:
        discount = 3
    elif location == 5:
        discount =12
    else:
        discount = "NO Discount Available"
elif product == 2:
    if location == 1:
        # India location
        discount = 20
    elif location == 2:
        #Pakistan
        discount = 15
    elif location == 3:
        #USA
        discount = 7
    elif location == 4:
        discount = 3
    elif location == 5:
        discount =12
    else:
        discount = "5"
elif product == 3:
    if location == 1:
        # India location
        discount = 20
    elif location == 2:
        #Pakistan
        discount = 15
    elif location == 3:
        #USA
        discount = 7
    elif location == 4:
        discount = 3
    elif location == 5:
        discount =12
    else:
        discount = "Discount Will Available Soon!"
elif product == 4:
    if location == 1:
        # India location
        discount = 30
    elif location == 2:
        #Pakistan
        discount = 10
    elif location == 3:
        #USA
        discount = 40
    elif location == 4:
        discount = 7
    elif location == 5:
        discount =12
    else:
        discount = 6
elif product == 5:
    if location == 1:
        # India location
        discount = 25
    elif location == 2:
        #Pakistan
        discount = 20
    elif location == 3:
        #USA
        discount = 5
    elif location == 4:
        discount = 3
    elif location == 5:
        discount =4
    else:
        discount = "NO Discount Available"
else:
    discount = 10
    
print('Discount as per the location and product is: ', discount) 