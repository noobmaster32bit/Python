# f=open("E:\\Luminar\\Python\\fileio\\news.txt","r")

# for line in f:
#     words=line.rstrip("\n").split(" ")
#     print(words)
   
    # split mathrem kodkmbo output il \n kaanm ath kalayan vendi aahn .rstrip() use cheythitt .split() use cheythath

# total number of words
# f=open("E:\\Luminar\\Python\\fileio\\news.txt","r")
# count=0
# for line in f:
#     words=line.rstrip("\n").split(" ")
#     print(words)
#     count=count+len(words)
# # print(count)


# count of each word

f=open("E:\\Luminar\\Python\\fileio\\news.txt","r")
wc={}
for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1

print(wc)