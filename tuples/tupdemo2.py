st={10,20,"hello",True,10,20}
print(st)

# insertion order is not preserved
# duplicate not allowed


colours={"white","black","red","blue"}

#add()
colours.add("teal")
print(colours)

st1={"white","black","blue"}
st2={"pink","teal","white","black"}

#add,difference,union,intersection,pop,remove,discard

#remove command terminates the program if the desired element is not present
#discard command does not terminate the program in the same case

# intersect_lst=st1.intersection(st2)
# # print(intersect_lst)
# uni_lst=st1.union(st2)
# # print(uni_lst)
# diff_set=st1.difference(st2)
# print(diff_set)
# print(st1)
# st1.pop()
# print(st1)

# st1.remove("blue")
st1.discard("blue")
print(st1)
