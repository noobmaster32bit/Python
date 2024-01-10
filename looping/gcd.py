#find gcd or hcf of the given numbers

n1=(int(input("Enter number1 : ")))
n2=(int(input("Enter number2 : ")))
smallest=n1 if n1<n2 else n2 

i=1

while(i<=smallest):
    if(n1%i==0 and n2%i==0):
        gcd=i
    i+=1

print("GCD of ", n1,"and", n2, "is", gcd)    
lcm=(n1*n2)/gcd
print(f"lcm of {n1} and {n2} = {lcm}")