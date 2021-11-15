# Create a program that will ask for grade percentage. Display the equivalent 
# Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

print("VIEN ANGELO BERNALES|BSCOE 1-1 \n")

import math 

YourGrade = float(input("Input your grade: "))

math.ceil(YourGrade)

if YourGrade >= 97 and YourGrade <= 100:
    print("Grade/Mark: 1.0")
    print("EXCELLENT!")

elif YourGrade >= 94 and YourGrade < 96:
    print("Grade/Mark: 1.25")
    print("EXCELLENT!")

elif YourGrade >= 91 and YourGrade < 93:
    print("Grade/Mark: 1.5")
    print("VERY GOOD!")