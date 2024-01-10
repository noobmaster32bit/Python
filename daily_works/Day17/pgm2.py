#  2. Python program to check if the given string is a palindrome.

str=input("Enter a string : ")
rev=""
for i in range(len(str)-1,-1,-1):
    rev+=str[i]
# print(rev)

if rev==str:
    print(str, "is a palindrome")
else:
    print("Not a palindrome")

