start=int(input("Enter the start range :"))
end=int(input("Enter the end range :"))
sum=0
for n in range(start,end+1):
    if n%2==0:
        sum=sum+n
print(sum)