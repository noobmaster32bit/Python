# 1. The original list : [1, 3, 5, 1, 3, 2, 5, 4, 2] (user input)
# Matrix after grouping : [[1, 1], [2, 2], [3, 3], [4], [5, 5]]

# og_list=[1,3,5,1,3,2,5,4,2]
# og_list.sort()
# i=0
# matrix=[]
# while i < (len(og_list))-1:                            
#     j=i+1                                              
#     current_element=og_list[i]                         
#     next_element=og_list[j]                            
#     if current_element==next_element :                 
#         matrix.append([current_element,next_element])  
#     i+=1                                               
# print(matrix)                                          
og_list = [1, 3, 5, 1, 3, 2, 5, 4, 2]
og_list.sort()
matrix = []
elements = set()

for i in og_list:
    if i not in elements:
        if og_list.count(i) > 1:
            matrix.append([i, i])
        else:
            matrix.append([i])
        elements.add(i)

print(matrix)
