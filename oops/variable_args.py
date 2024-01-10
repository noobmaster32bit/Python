
# def add_numbers(*args): # *args accepts mutliuple number of arguments for a single function supports function overloading
#     return sum(args)

# print(add_numbers(10,20))



# def last(*args):
    # last_num=0
    # for n in args:
    #     num=n%10
    #     last_num+=num
    # return last_num
#     last_sum=[n%10 for n in args]
#     return sum(last_sum)
    
# print(last(12,69,7))


#
# def last_digit(*args):
#     return max(n%10 for n in args)

# print(last_digit(19,28,77))

# **kwargs

# def add_employee(**kwargs):
#     print(kwargs.get("name"))
#     print(kwargs.get("salary"))


# add_employee(id=10, name="hari", n_place="ekm", w_place="tvm", salary=35000)


def last_digit_sort(*args,**kwargs):
    digit=[n%10 for n in args]
    value=kwargs.get("reversed")
    if value==True:
        digit.sort(reverse=True)
    else:
        digit.sort(reverse=False)
    return digit

print(last_digit_sort(17,89,52,68,reversed=False))

