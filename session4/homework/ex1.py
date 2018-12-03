items = ["T-shirt","Sweater"]
while True:
    action = input("Welcome to our shop, what do you want?(C,R,U,D,E): ")
    if action == "R":                           #Action R
        print("Our items:", end=" ")
        print(*items,sep=", ")

    if action == "C":                           #Action C
        n = input("Enter new items: ")
        items.append(n)
        print("Our items:", end=" ")
        print(*items,sep=", ")

    if action == "U":                           #Action U
        print("Our items:", end=" ")
        print(*items,sep=", ")
        while True:
            m = input("Update value: ")
            if m.isdigit():
                m_int = int(m)
                if m_int > 0 and m_int <=len(items):            #using position
                    n = input("Enter new items: ")
                    items[m_int-1]=n
                    break
                else:
                   print("Please enter a valid value!")
            elif m in items:
                n = input("Enter new items: ")                  #using value
                pos = items.index(m)
                items[pos]= n
                break
            else:
                print("Please enter a valid value!")
        print("Our items:", end=" ")
        print(*items,sep=", ")

    if action == "D":                           #Action D
        while True:
            m = input("Delete which?: ")
            if m.isdigit():
                m_int = int(m)
                if m_int > 0 and m_int <= len(items):           #using position
                    items.pop(m-1)
                    break
                else:
                    print("Please enter a valid value")
            elif m in items:                                    #using value
                items.remove(m)
                break
            else:
                print("Please enter a valid value")
        print("Our items:", end=" ")
        print(*items,sep=", ")

    if action == "E":                           #Exit program
        print("Bye Bye")
        break