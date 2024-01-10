# 2.Write a python program to accept decimal number and display it’s binary number

num=int(input("Enter a number: "))
binary = ''
while num > 0:
  binary = str(num % 2) + binary
  num //= 2
print(binary)
