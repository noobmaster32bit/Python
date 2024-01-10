text="ABCABBDE"

wc={}

for ch in text:
    if ch in wc:
        print(f"{ch} is the recurring character")
        break
    else:
        wc[ch]=1
