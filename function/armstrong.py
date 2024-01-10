def is_armstrong(num):
    num = int(num)
    real_num=num
    num_str = str(num)  
    length = len(num_str)
    sum = 0

    while num != 0:
        digit = num % 10
        exp=digit**length
        sum=sum+exp
        num=num//10

    return True if sum==real_num else False

print(is_armstrong(11))
