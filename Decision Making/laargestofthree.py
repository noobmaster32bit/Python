num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))

if (num1>num2 and num1>num3):
    print(f"{num1} is largest")

if (num2>num1 and num2>num3):
    print(f"{num2} is largest")

if (num3>num1 and num3>num1):
    print(f"{num3} is largest")

elif (num1==num2 and num3):
    print("equal")
