height=int(input("Enter height in cm : "))
weight=int(input("Enter weight in kg : "))
height_in_m=height/100

bmi=weight/(height_in_m)**2
# print(bmi)


if bmi<19:
    print("Underweight")

elif bmi<25:  
    print("healthy")

elif bmi<30:  
    print("overweight")
else:
    print("Obese")