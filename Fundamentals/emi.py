principal_amount=int(input("ENter the principal loan amount :"))
annual_interest=float(input("ENter the annual interest rate: "))
tenure_in_years=int(input("Enter the period of loan :"))

monthly_interest=((annual_interest/100)/12)
monthly_tenure=tenure_in_years*12

emi = principal_amount*monthly_interest*((1+monthly_interest)**monthly_tenure)/(((1+monthly_interest)**monthly_tenure)-1)
print("The monthly EMI for the loan is: ", round(emi))
