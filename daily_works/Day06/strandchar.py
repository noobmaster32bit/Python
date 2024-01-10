#  Write a Python program that accepts a string and calculates the number of digits and letters.
str=input("Enter a string : ")
letter_count=0
digit_count=0

for char in str:
    if char.isalpha():
        letter_count+=1
    elif char.isdigit():
        digit_count+=1

print("Number of letters =",letter_count)
print("Number of digits =",digit_count)