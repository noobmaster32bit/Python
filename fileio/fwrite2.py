# path="E:\\Luminar\\Python\\fileio\\years.txt"

# f=open(path,"w")

# for years in range(1800,2025):
#     if years%100==0:
#         f.write(str(years)+"\n")

# for year in range(1800,2025):
#     f.write(str(year)+"\n")

#read all years from years.txt and print only leap years


# path="E:\\Luminar\\Python\\fileio\\years.txt"

# f=open(path,"r")

# for line in f:
#     year=int(line.rstrip("\n"))
#     if year%100==0 and year%400==0 or year%4==0 and year%100!=0:
#         print(year)

read_path="E:\\Luminar\\Python\\fileio\\years.txt"
write_path="E:\\Luminar\\Python\\fileio\\leap_years.txt"

fr=open(read_path,"r")
fw=open(write_path,"w")

for line in fr:
    year=int(line.rstrip("\n"))
    if year%100==0 and year%400==0 or year%4==0 and year%100!=0:
        fw.write(str(year)+"\n")


