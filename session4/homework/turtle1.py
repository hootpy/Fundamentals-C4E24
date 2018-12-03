from    turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for n in range(3,8):
    for i in range(n):
        color(colors[n-3])
        forward(200)
        left(360/n)
        

mainloop()