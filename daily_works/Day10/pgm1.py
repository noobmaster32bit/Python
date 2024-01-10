# 1. Write a Python program that ask users to enter a number and keep asking the users to enter a correct number, until the number with in the range that we given

start=int(input("Enter a start range : "))
end=int(input("Enter end of the range : "))

while True:
    num=int(input("Enter a number :"))
    if num in range(start,end+1):
        print("The number is within the range")
        break
    else:
        print("Please enter a number within the range")
