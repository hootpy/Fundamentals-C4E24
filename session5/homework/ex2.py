price = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3
}
stock = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15
}
total = 0
for x in price:
    print(x)
    print("Price:",price[x])
    print("Stock:",stock[x])
    cost = price[x]*stock[x]
    total += cost
    print("Total:", cost)
    print("******************")

    
print("Total value:",total)