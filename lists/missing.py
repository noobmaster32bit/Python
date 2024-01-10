# arr=[1,6,3,7,4,5]
# arr.sort()
# i=0
# while i>(len(arr)-1):
#     j=i+1
#     jth_element=arr[j]
#     ith_element=arr[i]
#     diff=jth_element-ith_element
#     if (diff>1):
#         print(f"{ith_element+1} is missing")
#         break
#     i+=1

arr = [1, 6, 3, 7, 4, 5]
arr.sort()
i = 0
while i < (len(arr) - 1):
    j = i + 1
    jth_element = arr[j]
    ith_element = arr[i]
    diff = jth_element - ith_element

    if diff!=1:
        print(f"Element {ith_element+1} is missing")
        break
    i+=1
