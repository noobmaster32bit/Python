# def add(n1, n2):
#     res=n1+n2
#     return res

# print(add(10,20))


def smart_sub(n1, n2):
    res=n1-n2 if n1>n2 else n2-n1
    return res

print(smart_sub(10,20))


def cube(num=2):
    res=num **3
    return res

print(cube()) #8 no parameter passed but parameter set while fn defn
print(cube(4)) #64 parameter is passed so it overrides the parameter set while fn defn
