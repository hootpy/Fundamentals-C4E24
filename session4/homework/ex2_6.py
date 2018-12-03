flocks = [5,7,300,90,24,50,75]

print("Hello, my name is Hien and these are my sheeps size")
print(*flocks,sep=", ")
print()

for i in range(2):
    print("Month",i+1)

    for i2 in range(len(flocks)):
        flocks[i2] += 50
    print("One month has passed, now here is my flock")
    print(*flocks, sep=", ")

    n = flocks[0]
    for j in flocks:
        if n < j:
            n = j
    print("Now my biggest sheep has size",n,"let's shear it")


    pos = flocks.index(n)
    default_size = 8
    flocks[pos] = default_size
    print("After shearing, here is my block:")
    print(*flocks, sep=", ")
    
    print()

print("Month",i+2)
for i2 in range(len(flocks)):
    flocks[i2] += 50
print("One month has passed, now here is my flock")
print(*flocks, sep=", ")
print()

total_flocks = sum(flocks)

print("My flocks has size in total:", total_flocks)
print("I would get",total_flocks, "*2$: ", total_flocks*2,"$")

