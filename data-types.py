manifest = 'Flight: BA234 | Destination: Singapore | Passengers: 400'

# Strings are immutable cant be change
# manifest[0] = 'D'

#Indexing
print(manifest[8:14])
print(manifest[0:6])
print(manifest[14:40]) 
#Indexing me aesa hota hai
# ke agr 14 se 40 tk jo words show krta hai wo 39 tk hoty hain 
# 40 wla show nhi krta yani last ka number/words

#concatenation
gate = '| Gate: 12'
manifest += gate
print(manifest)

#length function for knowing how much characters are present in our string
total_chars = len(manifest)
print(f'Total characters in manifest: {total_chars}')

#Membership is nothing but used to find whether the value is present in the string or not
print('Gate' in manifest)

#Replication is way to multiply things multiple times

#like

print(manifest * 4)