words=["red", "green", "blue","violet"]

min_word=words[0]

for i in range(1,len(words)):
    current_word=words[i]
    if len(current_word)<len(min_word):
        min_word=current_word

print(min_word)
