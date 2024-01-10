n=int(input("Enter a number : "))
numbers=[]
for i in range (1,n+1):
    numbers.append(i)
numbers.reverse()
print("first",n,"natural numbers in descending order are",numbers)