import turtle
boom=turtle.Screen()
boom.bgcolor("black")
boom.title("selina")
pen=turtle.Turtle()
pen.speed(0)
colors=["red",'pink','purple','yellow','orange','green']
for  i in range(100):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 2)
    pen.left(120)
boom.exitonclick()