items = ["Books", "Games", "Movies"]

print("Here is your favorite thing so far", *items,sep=", ")



while True:
    n = int(input("Which one you want to delete?: "))
    if n > 0 and n <= int(len(items)):
        break
    else:
        print("Invalid Position")

items.pop(n-1)
print(*items)