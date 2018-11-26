a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
delta= b**2 -4*a*c
if delta<0:
    print("No answer")
elif delta==0:
    x= -b/(2*a)
    print("One answer:", x)
else:
    x1= (-b+delta**0.5)/2*a
    x2= (-b-delta**0.5)/2*a
    print("Two answer:",x1,x2)