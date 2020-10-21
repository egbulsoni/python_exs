import turtle

def swapFL(ls):
    ls[0], ls[-1] = ls[-1], ls[0]


ingredients = ['flour', 'sugar', 'butter', 'apples']

s = turtle.Screen()
t = turtle.Turtle()

def drawCircle(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(100)


def olympic(t):

    t.pensize(3)
    t.setheading(0)

    x = -200
    y = 60
    drawCircle(x,y)
    x += 226
    drawCircle(x, y)
    x += 226
    drawCircle(x, y)
    x = -200 + 113
    y -= 113
    drawCircle(x, y)
    x += 226
    drawCircle(x, y)

olympic(t)