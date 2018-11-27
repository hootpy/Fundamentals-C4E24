items = ["Books", "Games", "Movies"]

print("Here is your favorite thing so far", *items,sep=", ")


n = input("Name 1 thing you want to add: ")

items.append(n)

print(*items, sep=", ")