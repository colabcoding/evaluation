#understanding events
import turtle
import random

car = turtle.Turtle()

car.shape('circle')
car.size = 1

colours = ['red','orange','blue','green','purple','cyan','magenta','black']

def changecolor(x,y):
    car.color(random.choice(colours))
    car.size += 1
    car.shapesize(car.size)

def moveturtle(x,y):
    car.goto(x,y)

turtle.listen()

#click to change color
car.onclick(changecolor,1)
turtle.onscreenclick(moveturtle,1)

turtle.mainloop()