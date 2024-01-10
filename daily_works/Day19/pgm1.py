# 1. Write a python program to identify unique triplets whose three elements sum to zero from an array of n integers

def three_sum(nums):
    triplets=[]
    for i in range(0,len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if nums[i]+nums[j]+nums[k]==0:
                    triplets.append((nums[i],nums[j],nums[k]))
    return triplets

nums=[-3,-2,-1,0,1,2,3]
triplets=three_sum(nums)

if len(triplets)>0:
    print("Triplets whose sum is zero: ")
    for triplet in triplets:
        print(triplet)
else:
    print("No triplets found whose sum is zero")