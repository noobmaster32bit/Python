lst=[3,4,5,2]
sum=int(input("Enter the sum: "))
lst.sort()
for i in range(0,len(lst)-1):
    for j in range(i+1, len(lst)):
        cur_sum=lst[i]+lst[j]
        if sum==cur_sum:
            print(lst[i],lst[j])
            break