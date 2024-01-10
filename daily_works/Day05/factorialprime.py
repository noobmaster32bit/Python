num=int(input("Enter a number : "))
isPrime=True
fact=1

for i in range(2,num):
    if num%i==0:
        isPrime=False
        break
if isPrime:
    n=1
    while n<=num:
        fact=fact*n
        n=n+1
    print("factorial of",num, "is", fact )
else:
    print(num,"is not prime")




