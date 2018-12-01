tudien = {
    "hola": "xin chao",
    "adios": "tam biet",
    "buenos dias": "chao buoi sang",
    "buenas noches": "chao buoi toi",
    "hasta pronto": "hen gap lai",
}

while True:
    print(*tudien, sep=",")
    n = input("Look up?: ")
    if n in tudien:
        print(tudien[n])
    else:
        print("Not found!")

