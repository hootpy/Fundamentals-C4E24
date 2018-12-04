# person = {}
# print(person)

# person = {
#     "name": "H.Duc",
#     # "city": "Hai Phong",
# }

person = {
    "name": "H.Duc",
    "city": "Hai Phong",
    "age": 25,
}

person["age"] = 18
person["status"] = False

del person["city"]

print(person["age"])
print(person)
print("name" in person)

person["age"] += 1
print(person)