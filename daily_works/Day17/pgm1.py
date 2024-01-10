# 1. Create a program to print all the numbers in the range 10-50 excluding the multiples of 2 and 3

lst=[num for num in range(10,51) if num%2!=0 and num%3!=0]
print(lst)