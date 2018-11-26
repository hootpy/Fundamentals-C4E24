n = int(input("What were you born: "))
age = 2018 - n
print(age)

if age<10:
    print("Baby")
elif age<18:
    print("Teenager")
else:
    print("Adult")