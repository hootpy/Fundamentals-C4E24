items = ["Books", "Games", "Movies"]

print("Here is your favorite thing so far", *items,sep=", ")
m = len(items)
while True:
    n = str(input("Which one you want to delete?: "))
    for i in range(m):
        if n == items[i]:
            break
        
items.remove(n)

print(*items)