order1={"cb","tikka","fishfry","friedrice","vb","gheeroast"}
order2={"cb","friedrice","nan","upma","vegmeals","idly"}

union_order=order1.union(order2)
int_order=order1.intersection(order2)

order=union_order.difference(int_order)
print(order)


#predefined method for this 

new_order=order1.symmetric_difference(order2)
print(new_order)

st1={10,20,30}
st2={100,200,300}

st1.update(st2)
print(st1)