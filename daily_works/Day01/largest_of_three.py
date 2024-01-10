num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))
num3=int(input("Enter num3 :"))

largest=num1

if num2>largest:
    largest=num2
if num3>largest:
    largest=num3

print(largest)