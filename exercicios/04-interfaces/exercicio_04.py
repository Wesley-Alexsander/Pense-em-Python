import turtle
from math import pi

bob = turtle.Turtle()
turtle.bgcolor("black")
bob.color("orange")
bob.speed(100)

def polygon(*, T, n, length=100):
    angle = 360 / n
    T.pensize(2)
    for _ in range(n):
        T.forward(length)
        T.left(angle)
    turtle.mainloop()



def circle(r, n): 
    circumference = 2 * pi * r  # formula para calcular circunferencia
    length = circumference / n 
    print(circumference)
    print(length)
    polygon(T=bob, n=n, length=length)

# circle(200, 60)



# def exp():
#     for i in range(400):
#         bob.pensize(1)
#         bob.fd(i)
#         bob.rt(98)
#         bob.hideturtle()
#     turtle.mainloop()
# exp()