#     2. Write a program to filter the dictionary, from a dictionary of people’s heights and you wanted to filter out anyone below a certain height.

# Let’s filter out anyone less than 170cm.

height={"max":175,"appu":180,"ben":168,"greg":165,"simon":172}

for k,v in height.items():
    if v < 170:
        print(k)
        

