# # 2.Write a python program to find the least square number from a list

list=[5,4,7,3,8]
sq_list=[]
for num in list:
    square=num*num
    sq_list.append(square)
    num+=1
min_square=sq_list[0]
for n in range(len(sq_list)):
    if sq_list[n]<min_square:
        min_square=sq_list[n]

print("The minimum square is :", min_square)

