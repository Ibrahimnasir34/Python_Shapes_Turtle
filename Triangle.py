import turtle
ebra=turtle.Turtle()
ebra.color("white")
wn=turtle.Screen()
wn.bgcolor("black")
ebra.begin_fill()
ebra.fillcolor("red")

ebra.circle(100,steps=3) #add steps to make other shapes  .circle(radius,steps=3) for traiangle

ebra.end_fill()
ebra.hideturtle()