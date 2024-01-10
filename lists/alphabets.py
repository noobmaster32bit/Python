c4=["manoj","bilal","akash","malavika","jamina","akshay"]
vowels=[word for word in c4 if word[0]in ["a","e","i","o","u"]]
print(vowels)
cons=[word for word in c4 if word[0]not in ["a","e","i","o","u"]]
print(cons)


