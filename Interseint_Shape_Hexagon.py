import turtle
ebra=turtle.Turtle()
list1=["purple","red","orange","blue","green"]
for i in range(200):
    ebra.speed(3)
    ebra.color(list1[i%5])
    ebra.pensize(i/10+1)
    ebra.forward(i)
    ebra.left(59)