# 3.Pattern print 
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# * * * * * 
#  * * * * 
#   * * * 
#    * * 
#     *

for row in range(1,6):
    for col in range(row,6):
        print(end=" ")
    for col in range(row):
        print("*",end=" ")
    print("")
for row in range(1,6):
    for col in range(0,row):
        print(end=" ")
    for col in range(6,row,-1):
        print("*",end=" ")
    print()
