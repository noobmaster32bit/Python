# read number num
# print fizz if num / by 3
# print buzz if num / by 5
# print fizzbuzz if num/ by 15

num=int(input("enter a number:"))

if ((num%3==0)and(num%5==0)):
    print("fizzbuzz")

elif num %3==0:
    print("fizz")

elif num%5==0:
    print("buzz")
    

else:
    print("Nothing")