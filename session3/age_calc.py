while True:
    yob_str = input("When were you born: ")
    if yob_str.isdigit():
        break
yob = int(yob_str)

age = 2018 - yob
print(age)
