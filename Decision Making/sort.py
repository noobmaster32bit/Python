# sort 3 numbers
# if elif else 

num1=int(input("Enter a mumber:"))
num2=int(input("Enter a mumber:"))
num3=int(input("Enter a mumber:"))

if num1>num2 and num1>num3:

    if num2>num3:
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)
                
elif num2>num1 and num2>num3:

    if num1>num3:
        print(num2,num1,num3)
    else:
        print(num2, num3 ,num1)

elif num3>num1 and num3>num2:

    if num1>num2:
        print(num3, num1 ,num2)
    else:
        print(num3,num2 ,num1)

elif num1==num2 and num3:
    print("All equal")
    
    


      

# elif num2>num1 and num2>num3:
#     largest=num2
#     if num1>num3:
#         second_largest=num1
#         third_largest=num3
#     else:
#         second_largest=num3
#         third_largest=num1
#     print(f"{largest} ,{second_largest} ,{third_largest}")

# elif num3>num1 and num3>num2:
#     largest=num3
#     if num1>num2:
#         second_largest=num1
#         third_largest=num2
#     else:
#         second_largest=num2
#         third_largest=num1
#     print(f"{largest} ,{second_largest} ,{third_largest}")

# elif num1==num2 and num3:
#     print("All equal")



    