# print all century uears from starting year to current year


year = int(input("Enter the year:"))
current_year = 2023

while year <= current_year:
    if year % 100 == 0: 
        print(year)
    year +=1
