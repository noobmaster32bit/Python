# 2.Write a python program that Take input from user and make square list of the number and the cube list .Range is 10 number in the list

sq_lst=[]
cube_lst=[]

# num=int(input("Enter a number : "))
for num in range(0,10):
    square=num**2
    cube=num**3
    sq_lst.append(square)
    cube_lst.append(cube)

print(sq_lst)
print(cube_lst)