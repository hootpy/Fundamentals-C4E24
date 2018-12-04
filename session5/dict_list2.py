p1 = {
    "name": "H.Duc",
    "age": 25,
    "city": "Hai Phong"
}

p2 = {
    "name": "Hien",
    "age": 22,
    "city": "Nam Dinh"
}

p3 = {
    "name": "Long",
    "age": 19,
    "city": "Ha Noi"
}

p_list =[
    {
    "name": "H.Duc",
    "age": 25,
    "city": "Hai Phong"
    },
    {"name": "Hien",
    "age": 22,
    "city": "Nam Dinh"
    },
    {
    "name": "Long",
    "age": 19,
    "city": "Ha Noi"
    }
]
# print(p_list)

# p = p_list[0]
# print(p)
# print(p["name"])

for p in p_list:
    print(p["name"])
    print(p["city"])