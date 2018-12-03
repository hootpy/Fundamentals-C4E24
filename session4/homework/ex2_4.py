flocks = [5,7,300,90,24,50,75]

print("Hello, my name is Hien and these are my sheeps size")
print(*flocks,sep=", ")
print()
n = flocks[0]
for i in flocks:
    if n < i:
        n = i

print("Now my biggest sheep has size",n,"let's shear it")

j = flocks.index(n)
default_size = 8

flocks[j] = default_size

print("After shearing, here is my flocks")
print(*flocks, sep=", ")
print()

for i2 in range(len(flocks)):
    flocks[i2] += 50
print("One month has passed, now here is my flock:")
print(*flocks, sep=", ")
print()