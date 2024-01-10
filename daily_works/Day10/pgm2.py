# 2.Write a python program to list the even numbers from the range that given by the user and delete the multiplication of 5 from the list
start=int(input("Enter the start range : "))
end=int(input("Enter the end range : "))
numbers=[]

for i in range(start,end+1):
    if i%2==0:
        numbers.append(i)
    for n in numbers:
        if n%5==0:
            numbers.pop()
print(numbers)    