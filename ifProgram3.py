# Program 3: Life stages
# Create a program that ask for an age of a person
# Display the life stage of the person.

print("VIEN ANGELO BERNALES | BSCOE 1-1 \n")


GetAge = int(input("Please enter your age: "))

if GetAge > -1 and GetAge <= 12:
    print("KID")

elif GetAge >= 13 and GetAge <= 17:
    print("TEEN")

elif GetAge == 18:
    print("DEBUT")

else:
    print("ADULT")

print("DONE!")
