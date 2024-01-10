# colours=["red", "green", "blue", "white", "red", True, 123, 123.456]
# colours[1]="teal"
# print(colours)

#insertion order is preserved
#duplicates are allowed
#is mutable


expenses=[1200,1300,2300,4500,4200]

# for i in expenses:
#     print(i)

# for i in range(0,len(expenses)):
#     print(expenses[i])

#     #print all expenses>2500
# for i in range(0,len(expenses)):
#     if expenses[i]>2500:
#         print(expenses[i])


# for i in expenses:
#     if i>2500:
#         print(i)

        #print all expenses from 1500-2500

for i in range(0,len(expenses)):
    if expenses[i] in range (1500,2500):
        print(expenses[i])

max_exp=max(expenses)
min_exp=min(expenses)
total=sum(expenses)
print("maximum =",max_exp)
print("minimum =",min_exp)
print("total =",total)

avg=total/len(expenses)
print("average expense=",avg)


