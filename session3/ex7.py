cmd = str(input("What do you want (C, R, U ,D)?: "))
items=["Ga","Lon","Bo"]
if cmd == "C":
    n = input("What do you want to create?: ")
    items.append(n)

if cmd == "R":
    if len(items) == 0:
        print("There is nothing in here! Please add something!")
    else:
        print(*items)

if cmd == "U":
    if len(items) == 0:
        print("There is nothing to update!")
    else:
        print(items)
        while True:
            m = int(input("Which do you want to update?: "))
            if m > 0 and m <= len(items):
                upd = input("What do you want to change?: ")
                items[m - 1]= upd
                break


if cmd == "D":
    if len(items) == 0:
        print("There is nothing to delete!")
    else:
        print(items)
        while True:
            dele = input("Which one do you want to delete?:")
            if dele.isdigit():
                while True:
                    if int(dele) <= len(items):
                        items.pop(int(dele))
                        print("Deleted!")
                        break
                break
            elif dele.isalpha():
                for i in range(items):
                    if i == dele:
                        items.remove(dele)
                        print("Deleted!")
                break
            else:
                print("Can't find items!")

                    
print("Thank you!")