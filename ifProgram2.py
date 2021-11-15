# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

print("VIEN ANGELO BERNALES|BSCOE 1-1 \n")

# I tried to use a function
def GetNum():
    FirstNum = int(input("Enter the first number: "))
    SecondNum = int(input("Enter the second number: "))
    ThirdNum = int(input("Enter the third number: "))
    return FirstNum, SecondNum, ThirdNum

# call the function
NumberA, NumberB, NumberC = GetNum()
Smallest = 0

# use an if else statement
if NumberA < NumberB and NumberA < NumberC:
    Smallest = NumberA

elif NumberB < NumberC:
    Smallest = NumberB

else:
    Smallest = NumberC

print(Smallest, "is the lowest number.")