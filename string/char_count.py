text="!@12penumonoultramicroscopicsilicovolcanoconiosis"

# print(len(text))
# for ch in text:
#     print(ch)
v_count=0
for ch in text:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u": # for ch in ["a", "e", "i", "o", "u"] this is an alternative
        v_count+=1

print("The number of vowels is =", v_count)
print("The total number of words are =", len(text))

c_count=0

# if ch!="a" or ch!="e" or ch!="i" or ch!="o" or ch!="u":
#     c_count+=1

# print("The number of consonants is =", c_count)

for ch in text:
    if ch not in ["a", "e","i", "o", "u"]:
        if ch.isalpha():
            c_count+=1
print("The number of consonants is =", c_count)

