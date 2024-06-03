import turtle
import random
pat = turtle.Turtle()
turtle.Screen().bgcolor("gray")
colours = ["cyan", "purple", "white", "blue"]

pat = turtle.Turtle()

for i in range(10):
    for i in range(2):
        pat.forward(100)
        pat.right(60)
        pat.forward(100)
        pat.right(120)
    pat.right(36)
#pat.color(random.choice(colours))
pat.exitonclick()