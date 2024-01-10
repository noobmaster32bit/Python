prev=0
current=1
print(prev)

for num in range(1,11):
    next=prev+current
    if next%2==0:    
        print(next, "is even")
    else:
        print(next, "is odd")
    prev=current
    current=next

