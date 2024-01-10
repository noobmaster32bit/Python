# 2.Convert tuple to a list and find sum
tp=(1,5,6,4,8,0)
lst=[]
sum=0
for i in tp:
    lst.append(i)

for n in lst:
    sum+=n
print(sum)