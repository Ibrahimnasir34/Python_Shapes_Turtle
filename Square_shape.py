import turtle

ebra=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")

ebra.color("white")
# ebra.hideturtle()#turtle hide

ebra.speed(6)
print(help(turtle.speed()))
#simple without loop
# ebra.forward(100) #move 100 pic to east
# ebra.left(90) #degree movemnet of face of turtle
# ebra.forward(100)
# ebra.left(90) #degree movemnet of face of turtle
# ebra.forward(100)
# ebra.left(90) #degree movemnet of face of turtle
# ebra.forward(100)

ebra.begin_fill() #filling with color deafult black
ebra.fillcolor("blue")
for i in range(4):
    ebra.forward(100)  # move 100 pic to east
    ebra.left(90)  # degree movemnet of face of turtle
ebra.end_fill() #ending fillinf
ebra.hideturtle()
