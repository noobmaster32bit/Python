# create a fn to find nth root

def nth_root(num, n=2): #n=2 because if the value of n is not given the default value will be the square of the num
    res= num **n
    return res
print(nth_root(5))


def oneth_smallest(n1, n2):
    num1=n1%10
    num2=n2%10

    res= n1 if num1<num2 else n2
    return res

print (oneth_smallest(562,1001))

    
    
