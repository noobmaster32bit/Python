items=["bat", "ball", "stumps", "helmet", "Virat Kohli"]

longest=max(items,key=lambda w:len(w))
print(longest)

smallest=min(items,key=lambda w:len(w))
print(smallest)

total_char=sum(items)
print(total_char)


