items = ["Books", "Games", "Movies"]
m = len(items)
while True:
    n = int(input("Enter an index: "))
    if n < m and (n + m) > -1:
        break
    else:
        print("Your input is invalid!")
print(items[n])