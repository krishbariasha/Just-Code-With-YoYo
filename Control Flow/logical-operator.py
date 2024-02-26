'''
# true and true ======> True 
# or operator true or ture == True , False or False ===> false , true or false ==>
# true even if one of the boolean is true  it dosent care about others
not will always vconvert true to false and vice versa
'''
# And operator

is_weekend = True
is_sunny = True

if is_weekend and is_sunny:
    print('Lets go for the picnic')
else:
    print("We will go for the picnic next time")
    
# OR operator

is_novel = True
price = 50

if is_novel or price < 10:
    print('I will buy the book')
else:
    print('I will not buy the book')
    
    
# not operator

has_pasta = True

if not has_pasta:
    print('Time to order the pizza')
else:
    print('no need to order pizza')