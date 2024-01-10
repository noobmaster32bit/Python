def cube(n):
    return n**3
print(cube(3))
# cube lambda
cube=lambda n:n**3
print(cube(3))

# check positive or not
num_chk=lambda num:"+ve" if num>0 else "-ve" if num<0 else "zero"
print(num_chk(51))


# greatest of two nums
max_two=lambda n1, n2: n1 if n1>n2 else n2
print(max_two(3,75))

parity=lambda num: "even" if num%2==0 else "odd" 
print(parity(2))

# sort words according to the length of each word
text="good evening all"
words=text.split(" ") #split the words
print(words)

srt_words=sorted(words,key=lambda w:len(w), reverse=True) # sort the words, arrange in order of increasing length, reverse set to true for sorting words in decreasing order of length 
print(srt_words)

