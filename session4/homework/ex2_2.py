flocks = [5,7,300,90,24,50,75]

print("Hello, my name is Hien and these are my sheeps size")
print(*flocks,sep=", ")
n = flocks[0]
for i in flocks:
    if n < i:
        n = i

print("Now my biggest sheep has size",n,"let's shear it")