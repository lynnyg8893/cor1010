import turtle

turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

turtle.penup()
turtle.goto(-300, -200)
turtle.pendown()
turtle.width(50)

for color in colors:
    turtle.color(color)
    turtle.circle(300)
    turtle.right(90)

turtle.done()