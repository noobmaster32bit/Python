text="assei"

str=sorted(text)
print(str)


#ANAGRAM


source_word="won"
target_word="now"

txt1=sorted(source_word)
txt2=sorted(target_word)

print("true "if txt1==txt2 else "false")


print(text.startswith("as"))
print(text.endswith("as"))
print(text.count("s"))
print(text.index("e"))
txt3="@".join(text)
print(txt3)