# lst=[2,4,5,6,7,8,9]
# squares=[]

# for num in lst:
#     sq=num**2
#     squares.append(sq)
# print(squares)


# evens=[]
# for num in lst:
#     if num%2==0:
#         evens.append(num)

# print(evens)

#LIST COMPREHENSION

# [#return value for num in lst #condition]

lst=[2,4,5,6,7,8,9]
cubes=[num**3 for num in lst]
print(cubes)
squares=[num**2 for num in lst]
print(squares)

odd=[num for num in lst if num%2!=0]
print(odd)

c4=["manoj","bilal","akash","malavika","jamina","akshay"]
upper_names=[name.upper() for name in c4]
print(upper_names)

name_gt_four=[name for name in c4 if len(name)>4]
print(name_gt_four)

#start with vowels and start with cons
