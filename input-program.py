

# To calculate the radius of sphere and its volume

#the constant number of PI
PI = 3.14

#The input func in python
input_radius = input("Enter the radius of the Sphere: /n ~$")

# now we will perfrom the type cast
radius = float(input_radius)

#now calculate the surface area
surface_area = 4 * PI * radius ** 2

# mow we will calculate the volume of the sphere
volume = (4/3) * PI * radius ** 3

# its time to execute the results
print(f"The surface area of the sphere is: {surface_area}")

#now we will print the volume of the sphere
print(f'The Volume of the Sphere is: {volume}')


print("Thank U for Using It")