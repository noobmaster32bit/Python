# 3. Pattern print 
#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
rows=5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    print("*", end="")
    for j in range(2 * i - 1):
        print(" ", end="")
    if i != 0:
        print("*", end="")
    print()


for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end="")
    print("*", end="")
    for j in range(2 * i - 3):
        print(" ", end="")
    if i != 1:
        print("*", end="")
    print()
