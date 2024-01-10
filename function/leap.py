# is_leap_year


# is_armstrong
def is_leap_year(year):
    res= True if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else False
    return res

print(is_leap_year(2024))

#OR
# def is_leap_year(year):
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         return True
#     else:
#         return False
    
# print(is_leap_year(2024))