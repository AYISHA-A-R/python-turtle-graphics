import turtle
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
for i in range(300):
    t.pencolor(colors[i % 6])
    t.forward(i * 2)
    t.right(61)
turtle.done()