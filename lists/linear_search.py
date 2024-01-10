lst=[10,2,11,5,7,20]
element=int(input("Enter the element: "))
is_present=False

for i in range(0,len(lst)):
    curr_element=lst[i]
    if curr_element==element:
        is_present=True
        break
print(is_present)
