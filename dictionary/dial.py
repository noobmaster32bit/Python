dials={
    "1":["a","b","c"],
    "2":["d","e","f"],
    "3":["g","h","i"]
}
user_input="12"

print(dials.get(user_input))

for ch in user_input:
    if ch in dials.get(ch):