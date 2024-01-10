start_year=int(input("Enter start year : "))
end_year=int(input("Enter end year : "))


for year in range(start_year, end_year):
    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
        print(year)



