#factorial
num=1
def factorial(num):
    i=1
    fact=1
    while i<=num:
        fact=fact*i
        i+=1
    return fact

    # fact=1
    # for i in range(1,num+1):
    #     fact=fact*i
    # return fact

print(factorial(5))    