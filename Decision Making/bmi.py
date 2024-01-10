weight_inkg=int(input("Enter your weight in kg:"))
height_incm=int(input("Enter your height in cm:"))

height_inm=height_incm/100

bmi=weight_inkg/(height_inm**2)
print(bmi)

if bmi<19:
    print("Underweight")

elif bmi>=19 and bmi<25:  #bmi<25
    print("healthy")

elif bmi>=25 and bmi<30:  #bmi<30
    print("overweight")

elif bmi>=30 and bmi<40: #bmi<40
    print("obesity")

else:
    print("severely obese")