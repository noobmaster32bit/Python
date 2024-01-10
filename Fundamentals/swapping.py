num1=10
num2=20 

print(f"before swapping num1={num1} & num2={num2}")

#swapping logic
temp=num1
num1=num2
num2=temp

#OR

num1=num1+num2 #num1=10+20=30 ; num1=30
num2=num1-num2 #num2=30-20=10  ;num2=10
num1=num1-num2 #mum1=30-10=20  ;num1=20

#OR
#exclusive for python only
(num1,num2)=(num2,num1)

print(f"after swapping num1={num1} & num2={num2}")
