mobile={"id":100,"name":"iphone15","price":100000,"imei":2345,"processor":"B17"}
#print all key-value pairs
for k,v in mobile.items():
    print(k,v)

#print price
print(mobile.get("price"))

# update prica as rs 85000
mobile.update({"price":85000})

# remove imei
print(mobile.pop("imei"))

# print(mobile)


###### add a new key-value pair ######

# mobile.update({"offer":1000})
# or
mobile["offer"]=1000

#increase price by 1000
mobile["price"]+=1000
print(mobile)

print("colour" in mobile)