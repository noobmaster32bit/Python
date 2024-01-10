for row in range(1,6):
    for col in range(row,6):
        print(" ",end="")
    for col in range(1,row+1):
        print("*",end=" ")
    print()
