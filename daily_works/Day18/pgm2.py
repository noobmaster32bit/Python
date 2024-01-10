#   2.	Write a program to calculate the electricity bill. Accept the number of units consumed from the user
# Unit                        Price
# First 100 units      No charge
# Next 100 units     Rs 5 per unit
# After 200 units    Rs 10 per unit
# For example if input unit is 350 then total bill amount is Rs 2000

# 100   100      150
#  0   100*5     150*10  = 1500+500

units_consumed=int(input("Enter the units consumed : "))

if units_consumed<=100:
    charge=0
elif units_consumed<=200:
    charge= (units_consumed-100)*5
else:
    charge= 100*5 + (units_consumed-200)*10
print("Rs.", charge, " is your electricity charge")
