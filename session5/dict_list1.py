person = {
    "name": "Hien",
    "age" : "21",
    "city" : "Hanoi",
    "books": ["tam quoc","tieu ngao giang ho","sapiens"]
}

# print(person["name"])
# print(person["books"])

books = person["books"]

print(person["books"][1])


for b in person["books"]:
    print(b)
# print(books[-1])