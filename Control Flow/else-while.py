'''

    while <condition>
        <statement>
    else executes only:
        <statement>
        
Else executes only when these condition are true:
    1. When the while loop condition becomes false
    2.when the loop didn't encounter any break

'''


counter = 1

while (counter <5):
    print(counter)
    counter += 1
else:
    print('All the item has proceed')

while (counter <=5):
    print(counter)
    counter += 1
else:
    print('All the item has proceed')

while (counter <5):
    print(counter)
    counter += 1
    if counter ==3:
        break
else:
    print('All the item has proceed')
    