
f = open("data.json")
text = f.read()
import json
tudien = json.loads(text)
# tudien = {
#     "hola": "xin chao",
#     "adios": "tam biet",
#     "buenos dias": "chao buoi sang",
#     "buenas noches": "chao buoi toi",
#     "hasta pronto": "hen gap lai",
# }

while True:
    print("This is current library: ", end="")
    print(*tudien, sep=", ")
    print("Type exit to shut down")
    n = input("Look up?: ").lower()
    if n in tudien:
        print(tudien[n])
        ask = input("Do you want to update? (Y/N)").upper()
        if ask == "Y":
            upd = input("Your transalation: ")
            tudien[n] = upd
            print("Updated!")
        elif ask == "N":
            print("Thank you!")
    elif n == "exit":
        break
    else:
        print("Not found!")
        ask2 = input("Do you want to add this word? (Y/N)").upper()
        if ask2 == "Y":
            udp2 = input("Your definition:")
            tudien[n] = udp2
        elif ask2 == "N":
            print("Thank you!")
        else:
            print("invalid input!")

with open("data.json","w") as text:
    text.write(json.dumps(tudien))

