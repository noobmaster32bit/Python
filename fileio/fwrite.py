# path="E:\\Luminar\\Python\\fileio\\years.txt"

# f=open(path,"w")

# f.write("hello")

path="E:\\Luminar\\Python\\fileio\\colors.txt"

f=open(path,"w")

colors=["blue", "red", "green"]

# f.write(colors)   only string can be written inside the write fn

for c in colors:
    f.write(c+"\n")

    