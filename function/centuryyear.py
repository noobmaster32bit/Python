def is_century_year (year):
     res= True if year%100==0  else False
     return res  
print(is_century_year(2024))