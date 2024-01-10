# key-value pairs


product={"code":1001,"name":"orange","price":35}

######### keys() returns all keys ##########
# for k in product.keys():
#     print(k)


######## values() return all values##########

# for v in product.values():
#     print(v)

############ items() #############

# for k,v in product.items():
#     print(k,v)

########################################## 
print(product.get("name"))

#product.get("key") no error and returns none for unknown value
# product["key"] shows error for unknown value

############### update a value ##################

# product["price"]=50
# print(product)

product.update({"name":"oranges"})

########## remove key-value pair #############
product.pop("price")
print(product)

