items = ["Books", "Games", "Movies"]

print("Here is your favorite thing so far", *items,sep=", ")

while True:
    n = int(input("Position you want to update?: "))
    if n > 0 and n <= int(len(items)):
        break 
    else:
        print("Invalid position!")
m = input("Your replacing favorite?: ")

items[n-1] = m
print(*items, sep=", ")