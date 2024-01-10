num1=int(input("Enter a num1 : ")) 
num2=int(input("Enter a num2 : ")) 
operator=input("Enter the operator : ")

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2) 
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    if num2!=0:
        print(num1/num2)
    else:
        print("Division by zero not possible")




