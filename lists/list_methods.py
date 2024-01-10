orders=["friedrice", "porotta", "gheeroast","beeffry"]

orders.append("beef roast")
print(orders)

print(orders.count("porotta"))
print(orders.index("beeffry"))

print(orders.pop())#removes the latest entry from the list also we can specify the index of the object to be removed 
print(orders)

orders.insert(2, "chillichicken")
print(orders)

orders.remove("gheeroast") #specify the object to be removed,
print(orders)


