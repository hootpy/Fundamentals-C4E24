p = [
    {
        "Name": "Huy",
        "VND per Hour": 20,
        "Hour": 25
    },
    {
        "Name": "Quan",
        "VND per Hour": 30,
        "Hour": 30
    },
    {
        "Name": "Duc",
        "VND per Hour": 25,
        "Hour": 15
    }
]
sum_wage= 0
print("Luong cua tung nguoi:")
# for i in p:
#     wage = i["VND per Hour"]*i["Hour"]
#     print(i["Name"],wage, sep=": ")
#     sum_wage += wage
# print("Total:",sum_wage)

wage = [x["VND per Hour"]*x["Hour"] for x in p]
print(wage)
total = sum(wage)
print(total)