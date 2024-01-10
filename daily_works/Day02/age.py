age1=int(input("Enter age1 : "))
age2=int(input("Enter age2 : "))
age3=int(input("Enter age3 : "))

if age1>age2 and age1>age3:
    if age2>age3:
        print(age1, "is oldest", age3, "is youngest")
    else:
        print(age1, "is oldest", age2, "is youngest")
elif age2>age1 and age2>age3:
    if age1>age3:
        print(age2, "is oldest", age3, "is youngest")
    else:
        print(age2, "is oldest", age1, "is youngest")
if age3>age2 and age3>age1:
    if age2>age1:
        print(age3, "is oldest", age1, "is youngest")
    else:
        print(age3, "is oldest", age2, "is youngest")
        
