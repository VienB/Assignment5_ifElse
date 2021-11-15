# Create a program that will ask for grade percentage. Display the equivalent 
# Grade/Mark and Description
# Example:
# Input grade: 87.6
# Grade/Mark: 1.75
# Description: Very Good

print("VIEN ANGELO BERNALES|BSCOE 1-1 \n")

import math 

YourGrade = math.ceil(float(input("Input your grade: ")))

if YourGrade >= 97 and YourGrade <= 100:
    print("Grade/Mark: 1.0")
    print("EXCELLENT!")

elif YourGrade > 93 and YourGrade < 97:
    print("Grade/Mark: 1.25")
    print("EXCELLENT!")

elif YourGrade > 90 and YourGrade < 94:
    print("Grade/Mark: 1.5")
    print("VERY GOOD!")

elif YourGrade > 87 and YourGrade < 91:
    print("Grade/Mark: 1.75")
    print("VERY GOOD!")

elif YourGrade > 84 and YourGrade < 88:
    print("Grade/Mark: 2.0")
    print("GOOD!")

elif YourGrade > 81 and YourGrade < 85:
    print("Grade/Mark: 2.25")
    print("GOOD!")

elif YourGrade > 78 and YourGrade < 82:
    print("Grade/Mark: 2.5")
    print("SATISFACTORY")

elif YourGrade > 75 and YourGrade < 79:
    print("Grade/Mark: 2.75")
    print("SATISFACTORY")

elif YourGrade == 75:
    print("Grade/Mark: 3.0")
    print("PASSING")

elif YourGrade > 64 and YourGrade < 75:
    print("Grade/Mark: 5.0")
    print("FAILURE")
