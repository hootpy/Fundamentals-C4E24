person = {
    "name": "Hien",
    "age" : "21",
    "city" : "Hanoi",
    "books": ["tam quoc","tieu ngao giang ho","sapiens"]
}

print(person)

for k in person:                          #lay theo key
    print(k, person[k], sep=": ")


# for v in person.values():                 #lay theo value
#     print(v)

# for k,v in person.items():                #lay theo key va value
#     print(k,v, sep=": ")