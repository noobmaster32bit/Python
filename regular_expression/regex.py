from re import *
string="ababab"
pattern="ab"

match=finditer(pattern,string)

print(match)