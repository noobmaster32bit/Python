arr=[4,9,5,6,9,5,4]
arr.sort()
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        ith_element=arr[i]
        jth_element=arr[j]
        if ith_element-jth_element==0:
            print(ith_element)
            break



# arr=[4,9,5,6,9,5,4]
# seen=set()
# for i in arr:
#     if arr.count(i)>1 and i not in seen:
#         print(i)
#         seen.add(i)

        #find missing +ve integer
   
        