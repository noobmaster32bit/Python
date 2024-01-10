def calculator(*args,**kwargs):

    num=[n for n in args]
    value=kwargs.get("op")
    if value=="+":
        print(sum(num))

    elif value=="-":
        sub=0
        for i in num:
            sub=sub-i
        print(sub)


    elif value=="*":
        product=1
        for i in num:
            product=product*i
        print(product)



print(calculator(432,234,123,453,567,op="*"))
