# 1. Write a Python program that separate positive and negative numbers from a list
lst=[-3,8,9,-7,1,-4,-5]
positive_lst=[]
negative_lst=[]

for ch in lst:
    if ch>0:
        positive_lst.append(ch) 
    else:
        negative_lst.append(ch)

print("Positive list : ",positive_lst)
print("Negative list : ",negative_lst)


