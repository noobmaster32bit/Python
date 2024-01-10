vehicles=[
    {"id":"1","name":"passionpro","brand":"hero","price":"100000"},
    {"id":"2","name":"xpulse","brand":"hero","price":"140000"},
    {"id":"3","name":"triumph","brand":"triumph","price":"300000"},
    {"id":"4","name":"hunter","brand":"royal","price":"200000"},
    {"id":"5","name":"ola sl","brand":"ola","price":"170000"},
    {"id":"6","name":"ather 400","brand":"ather","price":"180000"}
]
# print name of all vehicles
# vehicles is a list, with some dictionaries
# so to access any values,  use the method to access value from a dictionary 
# ie, dictionary_name.get("key")
for bike in vehicles:
    print(bike.get("name"))


#print brand of all vehicles
for bike in vehicles:
    print(bike.get("brand"))


# print bikes with brand "hero"
for bike in vehicles:
    if bike.get("brand")=="hero":
        print(bike.get("name"))


# bikes under 150000
for  bike in vehicles:
    if bike.get("price")<"150000":
        print(bike.get("name"))

#costly bike

costly_bike=max(vehicles, key=lambda d:d.get("price"))
print(costly_bike)

low_cost=min(vehicles, key=lambda d:d.get("price"))
print(low_cost)