# 3. Pattern print 
# A 
# B B 
# C C C 
# D D D D 
# E E E E E

letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index=0
for row in range(1,6):
    for col in range(1,row+1):
        print(letters[index],end=" ")
    index+=1
    print()