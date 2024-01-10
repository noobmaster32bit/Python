#        3. Pattern print 
#       A 
#      A B 
#     A B C 
#    A B C D 
#   A B C D E

letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index=0

for row in range(1,6):
    for col in range(row,6):
        print(end=" ")
    for col in range(1,row+1):
        print(letters[col-1],end=" ")
    print("")

