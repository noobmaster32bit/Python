start_year=int(input("Enter the year: "))

current_year=2023
i=start_year

while(i<=current_year):
    year=i
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)
    i+=1    