# 2.Write a python program to reverse the tuple

tup=(1,2,3,4,5)
reverse_tup=[] 
for n in range(len(tup),0,-1):
    reverse_tup.append(n)
print(tuple(reverse_tup))
