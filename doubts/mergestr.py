# slicing
# [start:stop:step] # working is start:stop-1:step
#by default, start is 1 for positive indexing
name="Technolab"

# print(name[2:4]) #ch
# print(name[2:]) #chnolab
# print(name[:4]) #Tech

#----negative indexing----

# print(name[::-1]) # reverse the string
# print(name[-1:-5:-1]) # balo
# print(name[:-5:-1]) # balo
# print(name[-1::-1]) # reverse

# palindrome nu use cheyya

# first string nte number of words il koodthal ullath str2 il ninn print aakkanam
# string1="hello"
# string2="gummoningg"

# len1=len(string1)

# rem=string2[len1:]
# print(rem)


# --------------MERGE STRING--------------

str1="ABC"
str2="PQRST"

result=""
    # the string concatenation should work until the length of the minimum string 
minimum=min(len(str1),len(str2))
for i in range(0,minimum): # now the string will be sliced till the length of minimum string
    out=str1[i]+str2[i]
    result+=out

#slicing
if len(str1)>len(str2):  # the 2 string will be sliced to the same size 
    rem=str1[minimum:]
else:
    rem=str2[minimum:]

# the remaining will be added to the resulting string
result+=rem

print(result)

# ----------------------------------------
