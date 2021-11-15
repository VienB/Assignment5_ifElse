# Program 2: Find the lowest number
# Create a program that ask 3 numbers. 
# Find the lowest number using only if-else statement.
# Display the lowest number

def GetNum():
    FirstNum = int(input("Enter the first number: "))
    SecondNum = int(input("Enter the second number: "))
    ThirdNum = int(input("Enter the third number: "))
    return FirstNum, SecondNum, ThirdNum

NumberA, NumberB, NumberC = GetNum()
Smallest = 0

if NumberA < NumberB and NumberA < NumberC:
    Smallest = NumberA

print(Smallest, "is the lowest number.")