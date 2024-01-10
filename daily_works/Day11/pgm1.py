# 1. Write a Python program that print 2 list and common element

lst1=[7,9,4,3,5,10]
lst2=[1,8,7,0,3,9]
common=[]
for i in lst1:
    if i in lst2:
        common.append(i)
        i+=1

print("The common elements are : ",common)