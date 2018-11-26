n = int(input("Enter a number:"))
if n%2==0:
    for i in range(int(n/2)):
        print("x *",end=" ")
    print()
else:
    for i in range(int((n-1)/2)):
        print("x *",end=" ")
    print("x")