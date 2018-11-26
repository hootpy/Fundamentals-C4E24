from turtle import *

for n in range(3,7):
    if n%2!=0:
        color("blue")
    else:
        color("red")
    for i in range(n):
        forward(200)
        left(360/n)
    


mainloop()