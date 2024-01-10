words=["red", "green", "blue","violet"]

max_word=words[0]

for i in range(1,len(words)):
    current_word=words[i]
    if len(current_word)>len(max_word):
        max_word=current_word

print(max_word)


#min_word
#sum