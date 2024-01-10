principal_amt=int(input("Enter the principal amount : "))
rate=int(input("Enter the rate of interest : "))
years=int(input("Enter the  number of years : "))

ci=principal_amt*(1+(rate/100))**years-principal_amt

print(float(ci))