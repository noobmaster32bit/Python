# 4.Pattern print 
    #     A 
    #    B C 
    #   D E F 
    #  G H I J 
    # K L M N O
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index = 0
for row in range(1, 6):
    for col in range(row, 6):
        print(" ", end="")
    
    for col in range(1, row + 1):
        print(letters[index], end=" ")
        index += 1
    print()


